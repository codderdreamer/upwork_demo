import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
from kivy.config import Config
Config.set('kivy','keyboard_mode', 'dock')
Config.set('graphics', 'rotation', '0')
from ast import Str
import asyncio
import imp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.app import async_runTouchApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
import time
import random
import threading
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
from kivymd.app import MDApp
from kivy.clock import Clock
from functools import partial
from multiprocessing import Process, Manager
import keyboard
from kivy.uix.vkeyboard import *
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
import webbrowser

class HomeWindow(Screen):
    def __init__(self, wifiApp, **kw):
        self.wifiApp = wifiApp
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        wifi_connected = False
        if wifi_connected:
            threading.Thread(target=self.open_visi_help_window,daemon=True).start()
        else:
            threading.Thread(target=self.open_wifi_selector_window,daemon=True).start()
        return super().on_enter(*args)
    
    def open_visi_help_window(self):
        pass

    def open_wifi_selector_window(self):
        # time.sleep(10)
        self.wifiApp.openWifiSelectorWindow()
    
    def on_pre_leave(self, *args):
        return super().on_pre_leave(*args)
    
    def on_leave(self, *args):
        return super().on_leave(*args)
    
class WifiSelectorWindow(Screen):
    def __init__(self, wifiApp, **kw):
        self.wifiApp = wifiApp
        self.startNumber = -1
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        self.wifiApp.wifi_selector_window.startNumber = -1
        if len(self.wifiApp.active_wifi_names) > 0:
            self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = ""
            self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[0]
            if len(self.wifiApp.active_wifi_names) > 1:
                self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[1]
        else:
            print("Wifi bulunamadı!")

        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        # time.sleep(5)
        return super().on_enter(*args)
    
    def on_pre_leave(self, *args):
        return super().on_pre_leave(*args)
    
    def on_leave(self, *args):
        return super().on_leave(*args)

    
class WifiPasswordWindow(Screen):
    def __init__(self, wifiApp, **kw):
        self.wifiApp = wifiApp
        super().__init__(**kw)
        self.eng_keyboard_add()

    def on_pre_enter(self, *args):
        # self.eng_keyboard_add()
        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        return super().on_enter(*args)
    
    def on_pre_leave(self, *args):
        return super().on_pre_leave(*args)
    
    def on_leave(self, *args):
        return super().on_leave(*args)


    def add_mdcard(self,pos_hint,key_x,key_y):
        widget_card = MDCard()
        self.ids["key_" + str(key_x) + "_" + str(key_y)] = widget_card
        widget_card.size_hint = 0.06,0.15
        widget_card.radius = 6,6,6,6
        widget_card.pos_hint = pos_hint 
        widget_card.md_bg_color = get_color_from_hex("#465966")
        widget_card.ripple_behavior: True
        widget_card.elevation = True
        return widget_card
    
    def add_top_label(self,text):
        widget_label = MDLabel()
        widget_label.size_hint = 0.5,0.5
        widget_label.text = text
        widget_label.theme_text_color = "Custom"
        widget_label.font_size = "25sp"
        widget_label.font_name = "font/SF-Pro-Rounded-Medium.otf"
        widget_label.text_color = get_color_from_hex("#f2eded")
        widget_label.pos_hint = {'center_x': 0.5,'center_y': 0.5}
        widget_label.halign = "center"
        return widget_label

    def add_main_label(self,text):
        widget_label = MDLabel()
        widget_label.size_hint = 0.3,0.3
        widget_label.text = text
        widget_label.theme_text_color = "Custom"
        widget_label.font_size = "20sp"
        widget_label.font_name = "font/SF-Pro-Rounded-Medium.otf"
        widget_label.text_color = get_color_from_hex("#f2eded")
        widget_label.pos_hint = {'center_x': 0,'center_y': 0.8}
        widget_label.halign = "center"
        return widget_label
    
    def add_keyboard_key(self,pos_hint,text_top,text_main,key_x,key_y):
        pos_hint = pos_hint
        mdcard = self.add_mdcard(pos_hint,key_x,key_y)
        top_label = self.add_top_label(text_top)
        main_label = self.add_main_label(text_main)
        mdcard.add_widget(top_label)
        mdcard.add_widget(main_label)
        self.ids.keyboard.add_widget(mdcard)


    def add_delete(self,key_x,key_y):
        widget_card = MDCard()
        widget_card.size_hint = 0.06,0.15
        widget_card.radius = 6,6,6,6
        widget_card.pos_hint = {'x': 0.91,'y': .9}
        widget_card.md_bg_color = get_color_from_hex("#465966")
        widget_card.ripple_behavior: True
        widget_card.elevation = True

        image = Image()
        image.source = "delete.png"
        image.size_hint = 0.5,0.5
        image.pos_hint = {'center_x': 0.5,'center_y': 0.5}

        widget_card.add_widget(image)

        self.ids.keyboard.add_widget(widget_card)
        self.ids["key_" + str(key_x) + "_" + str(key_y)] = widget_card

    def add_tab(self,key_x,key_y):
        widget_card = MDCard()
        widget_card.size_hint = 0.1,0.15
        widget_card.radius = 6,6,6,6
        widget_card.pos_hint = {'x': 0,'y': .72}
        widget_card.md_bg_color = get_color_from_hex("#465966")
        widget_card.ripple_behavior: True
        widget_card.elevation = True

        image = Image()
        image.source = "tab.png"
        image.size_hint = 0.5,0.5
        image.pos_hint = {'center_x': 0.5,'center_y': 0.5}

        widget_card.add_widget(image)

        self.ids.keyboard.add_widget(widget_card)
        self.ids["key_" + str(key_x) + "_" + str(key_y)] = widget_card

    def add_caps_lock(self,key_x,key_y):
        widget_card = MDCard()
        widget_card.size_hint = 0.12,0.15
        widget_card.radius = 6,6,6,6
        widget_card.pos_hint = {'x': 0,'y': .54}
        widget_card.md_bg_color = get_color_from_hex("#465966")
        widget_card.ripple_behavior: True
        widget_card.elevation = True

        image = Image()
        image.source = "caps_lock.png"
        image.size_hint = 0.4,0.4
        image.pos_hint = {'center_x': 0.5,'center_y': 0.5}

        widget_card.add_widget(image)

        self.ids.keyboard.add_widget(widget_card)
        self.ids["key_" + str(key_x) + "_" + str(key_y)] = widget_card

    def add_enter(self,key_x,key_y):
        widget_card = MDCard()
        widget_card.size_hint = 0.07,0.31
        widget_card.radius = 6,6,6,6
        widget_card.pos_hint = {'x': .9,'y': .38}
        widget_card.md_bg_color = get_color_from_hex("#465966")
        widget_card.ripple_behavior: True
        widget_card.elevation = True

        image = Image()
        image.source = "enter.png"
        image.size_hint = 0.4,0.4
        image.pos_hint = {'center_x': 0.5,'center_y': 0.5}

        widget_card.add_widget(image)
        self.ids.keyboard.add_widget(widget_card)
        self.ids["key_" + str(key_x) + "_" + str(key_y)] = widget_card

    def add_shift(self,key_x,key_y):
        widget_card = MDCard()
        widget_card.size_hint = 0.16,0.15
        widget_card.radius = 6,6,6,6
        widget_card.pos_hint = {'x': 0,'y': .36}
        widget_card.md_bg_color = get_color_from_hex("#465966")
        widget_card.ripple_behavior: True
        widget_card.elevation = True

        image = Image()
        image.source = "shift.png"
        image.size_hint = 0.4,0.4
        image.pos_hint = {'center_x': 0.5,'center_y': 0.5}

        widget_card.add_widget(image)

        self.ids.keyboard.add_widget(widget_card)
        self.ids["key_" + str(key_x) + "_" + str(key_y)] = widget_card

    def add_space(self,key_x,key_y):
        widget_card = MDCard()
        widget_card.size_hint = 0.8,0.15
        widget_card.radius = 6,6,6,6
        widget_card.pos_hint = {'x': 0.1,'y': .18}
        widget_card.md_bg_color = get_color_from_hex("#465966")
        widget_card.ripple_behavior: True
        widget_card.elevation = True

        self.ids.keyboard.add_widget(widget_card)
        self.ids["key_" + str(key_x) + "_" + str(key_y)] = widget_card

    
    def eng_keyboard_add(self):
        # ------------------------------------ 1. Satır ------------------------------------------ 13,0
        #     '     ~
        self.add_keyboard_key({'x': 0,'y': .9},"'","~",0,0)
        #       1       !
        self.add_keyboard_key({'x': 0.07,'y': .9},"1","!",1,0)
        #       2       @
        self.add_keyboard_key({'x': 0.14,'y': .9},"2","@",2,0)
        #       3       #
        self.add_keyboard_key({'x': 0.21,'y': .9},"3","#",3,0)
        #       4       $
        self.add_keyboard_key({'x': 0.28,'y': .9},"4","$",4,0)
        #       5       %
        self.add_keyboard_key({'x': 0.35,'y': .9},"5","%",5,0)
        #       6       ^
        self.add_keyboard_key({'x': 0.42,'y': .9},"6","^",6,0)
        #       7       &
        self.add_keyboard_key({'x': 0.49,'y': .9},"7","&",7,0)
        #       8       *
        self.add_keyboard_key({'x': 0.56,'y': .9},"8","*",8,0)
        #       9       (
        self.add_keyboard_key({'x': 0.63,'y': .9},"9","(",9,0)
        #       0       )
        self.add_keyboard_key({'x': 0.7,'y': .9},"0",")",10,0)
        #       -       _
        self.add_keyboard_key({'x': 0.77,'y': .9},"-","_",11,0)
        #       =       +
        self.add_keyboard_key({'x': 0.84,'y': .9},"=","+",12,0)
        # delete
        self.add_delete(13,0)
        # ------------------------------------ 2. Satır ------------------------------------------ 12, 1
        # tab
        self.add_tab(0,1)
        #       q       Q
        self.add_keyboard_key({'x': 0.11,'y': .72},"q","Q",1,1)
        #       w       W
        self.add_keyboard_key({'x': 0.18,'y': .72},"w","W",2,1)
        #       e       E
        self.add_keyboard_key({'x': 0.25,'y': .72},"e","E",3,1)
        #       r       R
        self.add_keyboard_key({'x': 0.32,'y': .72},"r","R",4,1)
        #       t       T
        self.add_keyboard_key({'x': 0.39,'y': .72},"t","T",5,1)
        #       y       Y
        self.add_keyboard_key({'x': 0.46,'y': .72},"y","Y",6,1)
        #       u       U
        self.add_keyboard_key({'x': 0.53,'y': .72},"u","U",7,1)
        #       i       I
        self.add_keyboard_key({'x': 0.6,'y': .72},"i","I",8,1)
        #       o       O
        self.add_keyboard_key({'x': 0.67,'y': .72},"o","O",9,1)
        #       p       P
        self.add_keyboard_key({'x': 0.74,'y': .72},"p","P",10,1)
        #       [       {
        self.add_keyboard_key({'x': 0.81,'y': .72},"[","{",11,1)
        #       \       |
        self.add_keyboard_key({'x': 0.88,'y': .72}, " \ ", " | " ,12,1)
        # ------------------------------------ 3. Satır ------------------------------------------ 12, 2
        # caps lock
        self.add_caps_lock(0,2)
        #       a       A
        self.add_keyboard_key({'x': 0.13,'y': .54},"a","A",1,2)
        #       s       S
        self.add_keyboard_key({'x': 0.2,'y': .54},"s","S",2,2)
        #       d       D
        self.add_keyboard_key({'x': 0.27,'y': .54},"d","D",3,2)
        #       f       F
        self.add_keyboard_key({'x': 0.34,'y': .54},"f","F",4,2)
        #       g       G
        self.add_keyboard_key({'x': 0.41,'y': .54},"g","G",5,2)
        #       h       H
        self.add_keyboard_key({'x': 0.48,'y': .54},"h","H",6,2)
        #       j       J
        self.add_keyboard_key({'x': 0.55,'y': .54},"j","J",7,2)
        #       k       K
        self.add_keyboard_key({'x': 0.62,'y': .54},"k","K",8,2)
        #       l       L
        self.add_keyboard_key({'x': 0.69,'y': .54},"l","L",9,2)
        #       ;       :
        self.add_keyboard_key({'x': 0.76,'y': .54},";",":",10,2)
        #       `       "
        self.add_keyboard_key({'x': 0.83,'y': .54}," ` "," \" ",11,2)
        # enter
        self.add_enter(12,2)
        # ------------------------------------ 4. Satır ------------------------------------------ 10, 3
        # shift
        self.add_shift(0,3)
        #       z       Z
        self.add_keyboard_key({'x': 0.17,'y': .36},"z","Z",1,3)
        #       x       X
        self.add_keyboard_key({'x': 0.24,'y': .36},"x","X",2,3)
        #       c       C
        self.add_keyboard_key({'x': 0.31,'y': .36},"c","C",3,3)
        #       v       V
        self.add_keyboard_key({'x': 0.38,'y': .36},"v","V",4,3)
        #       b       B
        self.add_keyboard_key({'x': 0.45,'y': .36},"b","B",5,3)
        #       n       N
        self.add_keyboard_key({'x': 0.52,'y': .36},"n","N",6,3)
        #       m       M
        self.add_keyboard_key({'x': 0.59,'y': .36},"m","M",7,3)
        #       ,       <
        self.add_keyboard_key({'x': 0.66,'y': .36},",","<",8,3)
        #       .       >
        self.add_keyboard_key({'x': 0.73,'y': .36},".",">",9,3)
        #       /       ?
        self.add_keyboard_key({'x': 0.8,'y': .36},"/","?",10,3)
        # ------------------------------------ 5. Satır ------------------------------------------ 0, 4
        # boşluk
        self.add_space(0,4)
        
class WebWindow(Screen):
    def __init__(self, wifiApp, **kw):
        self.wifiApp = wifiApp
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        return super().on_pre_enter(*args)
    
    def on_enter(self, *args):
        return super().on_enter(*args)
    
    def on_pre_leave(self, *args):
        return super().on_pre_leave(*args)
    
    def on_leave(self, *args):
        return super().on_leave(*args)
    


class WifiApp(MDApp):
    def __init__(self,app,loop,**kwargs):
        super().__init__(**kwargs)
        self.loop = loop
        self.app = app
        self.screenmanager = None
        self.home_window = None
        self.wifi_selector_window = None

        self.active_wifi_names = ["FiberHGW_TP06BA_5GHz", "DIRECT-3D-HP", "FiberHGW_TP06BA_2.4GHz", "Kurt Home", "My Home"]

        self.close = False
        self.close_async_run = None

        threading.Thread(target=self.main,daemon=True).start()

    def openHomeWindow(self):
        Clock.schedule_once(self.call_home_window, 0)


    def openWifiSelectorWindow(self):
        Clock.schedule_once(self.call_wifi_selector_window, 0)

    def openWifiPasswordWindow(self):
        Clock.schedule_once(self.call_wifi_password_window, 0)

    def openWebWindow(self):
        Clock.schedule_once(self.call_web_window, 0)


    def call_home_window(self,event):
        self.screenmanager.current_screen.manager.current = "HomeWindow"
        self.screenmanager.current_screen.manager.transition.direction = "left"

    def call_wifi_selector_window(self,event):
        self.screenmanager.current_screen.manager.current = "WifiSelectorWindow"
        self.screenmanager.current_screen.manager.transition.direction = "left"

    def call_wifi_password_window(self,event):
        self.screenmanager.current_screen.manager.current = "WifiPasswordWindow"
        self.screenmanager.current_screen.manager.transition.direction = "left"

    def call_web_window(self,event):
        self.screenmanager.current_screen.manager.current = "WebWindow"
        self.screenmanager.current_screen.manager.transition.direction = "left"

    def main(self):
        self.openHomeWindow()
        while self.close == False:
            print("hey")
            time.sleep(1)
        
    def build(self):
        # Window classes definition
        self.screenmanager = ScreenManager()

        self.home_window = HomeWindow(self,name="HomeWindow")
        self.wifi_selector_window = WifiSelectorWindow(self,name="WifiSelectorWindow")
        self.wifi_password_window = WifiPasswordWindow(self,name="WifiPasswordWindow")
        self.web_window = WebWindow(self,name="WebWindow")

        
        self.screenmanager.add_widget(self.home_window)
        self.screenmanager.add_widget(self.wifi_selector_window)
        self.screenmanager.add_widget(self.wifi_password_window)
        self.screenmanager.add_widget(self.web_window)


        return self.screenmanager
    
    
    
class Interface_Application:
    def __init__(self,loop) -> None:
        self.wifiApp = None
        self.loop = loop

        self.key_down_press = 0
        self.counter = 0

        self.password_right_counter = -1
        self.password_left_counter = -1
        self.password_up_counter = -1
        self.password_down_counter = -1

        self.old_x = 0
        self.old_y = 0

        self.evet_keyboard = True

        self.key_kontrol_stop = False

        threading.Thread(target=self.key_control, daemon=True).start()


    def key1(self):
        if self.evet_keyboard == True:
            print('************************* ctrl+shift+F1 ')
        self.evet_keyboard = False

    def key2(self):
        if self.evet_keyboard == True:
            print('************************* ctrl+shift+F2')
        self.evet_keyboard = False

    def key3(self):
        if self.evet_keyboard == True:
            print('************************* ctrl+shift+F3')
        self.evet_keyboard = False

    def key4(self):
        if self.evet_keyboard == True:
            print('************************* ctrl+shift+F4')
        self.evet_keyboard = False

    def key5(self):
        if self.evet_keyboard == True:
            print('************************* ctrl+shift+F5')
        self.evet_keyboard = False

    def key6(self):
        if self.evet_keyboard == True:
            print('************************* ctrl+shift+F6')
        self.evet_keyboard = False

    def key7(self):
        if self.evet_keyboard == True:
            print('************************* ctrl+shift+F7')
        self.evet_keyboard = False

    def key_up(self):
        if self.evet_keyboard == True:
            print('************************* up')
            if self.wifiApp.screenmanager.current_screen:
                if self.wifiApp.screenmanager.current_screen.manager.current == "WifiSelectorWindow":
                    print("WifiSelectorWindow","up")
                    self.wifiApp.wifi_selector_window.startNumber = self.wifiApp.wifi_selector_window.startNumber - 1

                    if len(self.wifiApp.active_wifi_names) - 2 == self.wifiApp.wifi_selector_window.startNumber:
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[0]
                        self.wifiApp.wifi_selector_window.startNumber = -2
                    elif self.wifiApp.wifi_selector_window.startNumber == -1:
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[len(self.wifiApp.active_wifi_names)-1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                    elif self.wifiApp.wifi_selector_window.startNumber == 0:
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                    else:
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                elif self.wifiApp.screenmanager.current_screen.manager.current ==  "WifiPasswordWindow":
                    pass
        self.evet_keyboard = False

    def key_down(self):
        if self.evet_keyboard == True:
            print('************************* down')
            if self.wifiApp.screenmanager.current_screen:
                if self.wifiApp.screenmanager.current_screen.manager.current == "WifiSelectorWindow":
                    print("WifiSelectorWindow","down")
                    self.wifiApp.wifi_selector_window.startNumber = self.wifiApp.wifi_selector_window.startNumber + 1

                    if len(self.wifiApp.active_wifi_names) - 2 == self.wifiApp.wifi_selector_window.startNumber:
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[0]
                        self.wifiApp.wifi_selector_window.startNumber = -2
                    elif self.wifiApp.wifi_selector_window.startNumber == -1:
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[len(self.wifiApp.active_wifi_names)-1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                    elif self.wifiApp.wifi_selector_window.startNumber == 0:
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                    else:
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_1.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_2.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+1]
                        self.wifiApp.wifi_selector_window.ids.wifi_name_label_3.text = self.wifiApp.active_wifi_names[self.wifiApp.wifi_selector_window.startNumber+2]
                elif self.wifiApp.screenmanager.current_screen.manager.current ==  "WifiPasswordWindow":
                    self.password_down_counter += 1
                    if self.password_down_counter == 5:
                        self.password_down_counter = 0
                    elif self.password_down_counter == -1:
                        self.password_down_counter = 0
                    if self.password_right_counter == -1:
                        self.password_right_counter = 0

                    if self.password_down_counter == 4:
                        self.password_right_counter = 0
                    elif self.password_down_counter == 3:
                        if self.password_right_counter > 9:
                            self.password_right_counter = 9
                    elif self.password_down_counter == 2 or self.password_down_counter == 1:
                        if self.password_right_counter > 11:
                            self.password_right_counter = 11
                    elif self.password_down_counter == 0:
                        if self.password_right_counter > 12:
                            self.password_right_counter = 12

                    
                    self.wifiApp.wifi_password_window.ids["key_" + str(self.old_x) + "_" + str(self.old_y)].md_bg_color = get_color_from_hex("#465966")
                    self.wifiApp.wifi_password_window.ids["key_" + str(self.password_right_counter) + "_" + str(self.password_down_counter)].md_bg_color = get_color_from_hex("#91b5cf")
                    self.old_x = self.password_right_counter
                    self.old_y = self.password_down_counter

        self.evet_keyboard=False




    def key_left(self):
        if self.evet_keyboard == True:
            print('************************* left')
            if self.wifiApp.screenmanager.current_screen:
                if self.wifiApp.screenmanager.current_screen.manager.current ==  "WifiPasswordWindow":
                    self.password_right_counter -= 1
                    if self.password_right_counter == -1 or self.password_right_counter == -2:
                        if self.password_down_counter == 0:
                            self.password_right_counter = 13
                        elif self.password_down_counter == 1 or self.password_down_counter == 2:
                            self.password_right_counter = 12
                        elif self.password_down_counter == 3:
                            self.password_right_counter = 10
                        elif self.password_down_counter == 4:
                            self.password_right_counter = 0
        
                    self.wifiApp.wifi_password_window.ids["key_" + str(self.old_x) + "_" + str(self.old_y)].md_bg_color = get_color_from_hex("#465966")
                    self.wifiApp.wifi_password_window.ids["key_" + str(self.password_right_counter) + "_" + str(self.password_down_counter)].md_bg_color = get_color_from_hex("#91b5cf")

                    self.old_x = self.password_right_counter
                    self.old_y = self.password_down_counter

        self.evet_keyboard = False

    def key_right(self):
        if self.evet_keyboard == True:
            print('************************* right')
            if self.wifiApp.screenmanager.current_screen:
                if self.wifiApp.screenmanager.current_screen.manager.current ==  "WifiPasswordWindow":
                    self.password_right_counter += 1
                    if self.password_down_counter == -1:
                        self.password_down_counter = 0
                    self.wifiApp.wifi_password_window.ids["key_" + str(self.old_x) + "_" + str(self.old_y)].md_bg_color = get_color_from_hex("#465966")
                    self.wifiApp.wifi_password_window.ids["key_" + str(self.password_right_counter) + "_" + str(self.password_down_counter)].md_bg_color = get_color_from_hex("#91b5cf")
                    self.old_x = self.password_right_counter
                    self.old_y = self.password_down_counter
                    # keyboard en sona gelmişse başa dönmesi için kullanıyorum
                    if self.password_down_counter == 0:
                        if self.password_right_counter == 13:
                            self.password_right_counter = -1
                    elif self.password_down_counter == 1 or self.password_down_counter == 2:
                        if self.password_right_counter == 12:
                            self.password_right_counter = -1
                    elif self.password_down_counter == 3:
                        if self.password_right_counter == 10:
                            self.password_right_counter = -1
                    elif self.password_down_counter == 4:
                        if self.password_right_counter == 0:
                            self.password_right_counter = -1

        self.evet_keyboard = False


    def key_enter(self):
        if self.evet_keyboard == True:
            print('************************* enter')
            if self.wifiApp.screenmanager.current_screen:
                if self.wifiApp.screenmanager.current_screen.manager.current == "WifiSelectorWindow":
                    print("WifiSelectorWindow","enter")
                    self.wifiApp.openWifiPasswordWindow()
                
        self.evet_keyboard = False

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

        while self.key_kontrol_stop == False:  # Loop to capture keys continuously
            print("event")
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
            


    async def run_app(self):
        '''This method, which runs Kivy, is run by the asyncio loop as one of the
        coroutines.
        '''
        # we don't actually need to set asyncio as the lib because it is the
        # default, but it doesn't hurt to be explicit
        await self.wifiApp.async_run(async_lib='asyncio')

        print(datetime.now(),'App done')

    def root_func(self):
        '''This will run both methods asynchronously and then block until they
        are finished
        '''
        self.wifiApp = WifiApp(self,self.loop)

        return asyncio.gather(self.run_app())
    
if __name__ == '__main__':
    Window.size = (1920, 1200)

    loop = asyncio.get_event_loop()
    app = Interface_Application(loop)

    loop.run_until_complete(app.root_func())
    loop.close()

