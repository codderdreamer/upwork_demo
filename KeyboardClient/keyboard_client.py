import keyboard
import os
import threading
from multiprocessing import Process, Manager
import asyncio
import websockets
import time
 

# İnternetin varlığını ve yokluğunu kontrol edecek
# İnternet yoksa web arayüzü kapatma keyboardunu gönderecek, kivy arayüzünü açmasını göndrecek
# İnternet varsa kivy arayüzünü kapatma keyboardunu gönderecek, web arayüzünü açmasını gönderecek
# Eğer ctrl+shift+1 e basılmışsa webi kapat, kivy arayüzünü açmasını göndrecek
# ctrl+shift+2 web sayfası açıksa Tarayıcıyı yenile, değilse aç
# ctrl+shift+3 çerezleri sil
# ctrl+shift+4 ekran yönü değiştir

async def send_message(data):
    async with websockets.connect('ws://127.0.0.1:8000') as websocket:
        await websocket.send(data)
        response = await websocket.recv()
        print(response)

class Application:
    def __init__(self):
        self.evet_keyboard = True


        self.key_down_press = 0
        self.connected = False

    

    def set_connected(self,value):
        if self.connected != value:
            self.connected = value
            if self.connected == False:
                keyboard.press_and_release('ctrl+alt+backspace')
                asyncio.set_event_loop(loop)
                asyncio.get_event_loop().run_until_complete(send_message("open kivy interface"))
            else:
                keyboard.press_and_release('esc')
                asyncio.set_event_loop(loop)
                asyncio.get_event_loop().run_until_complete(send_message("open web interface"))
                



    def key_control(self,loop):
        try:
            keyboard.add_hotkey('ctrl+shift+1', self.key1)
            keyboard.add_hotkey('ctrl+shift+2', self.key2)
            keyboard.add_hotkey('ctrl+shift+3', self.key3)
            keyboard.add_hotkey('ctrl+shift+4', self.key4)
            keyboard.add_hotkey('ctrl+shift+5', self.key5)
            keyboard.add_hotkey('ctrl+shift+6', self.key6)
            keyboard.add_hotkey('ctrl+shift+7', self.key7)
            keyboard.add_hotkey('up',self.key_up)
            keyboard.add_hotkey('down',self.key_down)
            keyboard.add_hotkey('right',self.key_right)
            keyboard.add_hotkey('left',self.key_left)
            keyboard.add_hotkey('enter',self.key_enter)
        except Exception as e:
            print("Keyboard exception",e)

        while True:  # Loop to capture keys continuously
            print("event keyboard")
            try:
                event = keyboard.read_event()
                print(event)
                self.evet_keyboard = True
                if event.event_type == keyboard.KEY_DOWN:
                    self.key_down_press += 1
                if event.event_type == keyboard.KEY_UP:
                    self.key_down_press = 0
                    self.counter = 0
            except Exception as e:
                print("Keyboard exception",e)

    def key1(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+1') 
            keyboard.press_and_release('esc')
            keyboard.press_and_release('ctrl+alt+backspace')
            asyncio.set_event_loop(loop)
            asyncio.get_event_loop().run_until_complete(send_message("open kivy interface"))
            print("here ctrl+shift+1")
        self.evet_keyboard = False

    def key2(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+2')
            keyboard.press_and_release('ctrl+alt+backspace')
            keyboard.press_and_release('esc')
            asyncio.set_event_loop(loop)
            asyncio.get_event_loop().run_until_complete(send_message("open web interface"))
            print("here ctrl+shift+2")
        self.evet_keyboard = False

    def key3(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+3')
        self.evet_keyboard = False

    def key4(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+4')
        self.evet_keyboard = False

    def key5(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+5')
        self.evet_keyboard = False

    def key6(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+6')
        self.evet_keyboard = False

    def key7(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+7')
        self.evet_keyboard = False

    def key_up(self):
        if self.evet_keyboard == True:
            print('*************************key: up')
        self.evet_keyboard = False

    def key_down(self):
        if self.evet_keyboard == True:
            print('*************************key: down')
        self.evet_keyboard=False

    def key_left(self):
        if self.evet_keyboard == True:
            print('*************************key: left')
        self.evet_keyboard = False

    def key_right(self):
        if self.evet_keyboard == True:
            print('*************************key: right')
        self.evet_keyboard = False


    def key_enter(self):
        if self.evet_keyboard == True:
            print('*************************key: enter')        
        self.evet_keyboard = False

    def is_network_connected(self):
        while True:
            try:
                print("scan_network")
                os.system('touch /home/pi/data/network_status.txt')
                os.system('chmod +rw /home/pi/data/network_status.txt')
                os.system('nmcli dev status > network_status.txt')
                file = open("network_status.txt",'r')
                lines = file.readlines()
                for line in lines:
                    print(line)
                    if (" connected" in line):
                        self.setconnected=True
            except Exception as e:
                print(e)
            time.sleep(5)


app = Application()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
threading.Thread(target=app.key_control,args=(loop,),daemon=True).start()
# threading.Thread(target=app.is_network_connected,daemon=True).start()

while True:
    time.sleep(1)


