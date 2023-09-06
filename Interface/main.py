import keyboard
import os
import threading
from multiprocessing import Process, Manager

class Application:
    def __init__(self):
        self.evet_keyboard = True
        self.key_down_press = 0


    def key_control(self):
        try:
            keyboard.add_hotkey('ctrl+shift+F1', self.key1)
            keyboard.add_hotkey('ctrl+shift+F2', self.key2)
            keyboard.add_hotkey('ctrl+shift+F3', self.key3)
            keyboard.add_hotkey('ctrl+shift+F4', self.key4)
            keyboard.add_hotkey('ctrl+shift+F5', self.key5)
            keyboard.add_hotkey('ctrl+shift+F6', self.key6)
            keyboard.add_hotkey('ctrl+shift+F7', self.key7)
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
            print('*************************key: ctrl+shift+F1')
        self.evet_keyboard = False

    def key2(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+F2')
        self.evet_keyboard = False

    def key3(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+F3')
        self.evet_keyboard = False

    def key4(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+F4')
        self.evet_keyboard = False

    def key5(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+F5')
        self.evet_keyboard = False

    def key6(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+F6')
        self.evet_keyboard = False

    def key7(self):
        if self.evet_keyboard == True:
            print('*************************key: ctrl+shift+F7')
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

app = Application()
app.key_control()
