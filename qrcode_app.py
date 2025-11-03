import pyqrcode
import os
def generate_QRCODE(data,file_name):
    main =pyqrcode.create(data)
    main.png(file_name,scale=6)
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton,MDFloatingActionButton,MDTextButton,MDRectangleFlatButton
from kivy.uix.image import Image,AsyncImage
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from random import choice
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.transition import MDSlideTransition
Window.size = (350, 600)

class menu_screen(MDScreen):
    def __init__(self,*args):
        super()
        self.name = 'menu'
        self.main = BoxLayout()
        self.main.orientation = 'vertical'
        self.titlebox = MDTopAppBar(title='clock')
        
class QRCODE(MDApp):
    def on_start(self):
        return super().on_start()
    def build(self):
        self.online = True
        self.filesa =  []
        self.root =MDScreenManager()
        self.titlebox = MDTopAppBar(title = 'QRCODE')
        self.titlebox.anchor_title = 'left'
        self.titlebox.left_action_items = [['menu',]]
        self.titlebox.right_action_items = [['clock',self.clock]]
        self.first_screen = MDScreen(name = 'first')
        self.clock_screen = MDScreen(name = 'clock')
        self.main = BoxLayout()
        self.main.add_widget(self.titlebox)
        self.send = BoxLayout()
        self.send.padding = '20dp'
        self.savebutton = MDFillRoundFlatButton(text= "SAVE",pos_hint = {'center_x':0.5,'center_y':0.9},on_release=self.save)
        self.main.orientation = 'vertical'
        if self.online:
            self.qrcode = AsyncImage()
        else:
            self.qrcode = Image(size_hint = (0.95,0.95))
        self.Entrybox = MDTextField(pos_hint = {'center_x':0.5,'center_y':0.5})
        self.Entrybox.hint_text = 'Enter data'
        self.Entrybox.active_line = True
        self.sendbutton = MDFillRoundFlatButton(text= 'CREATE',pos_hint = {'center_x':0.5,'center_y':0.5},on_release=self.work)
        menu = menu_screen()
        self.main.add_widget(self.qrcode)
        self.send.add_widget(self.Entrybox)
        self.send.add_widget(self.sendbutton)
        self.main.add_widget(self.send)
        self.main.add_widget(self.savebutton)
        self.first_screen.add_widget(self.main)
        self.root.add_widget(self.first_screen)
        self.root.add_widget(self.clock_screen)
        self.clock_init()
        return self.root
    def clock_init(self,):
        self.clock_main = BoxLayout()
        self.clock_main.orientation = 'vertical'
        self.clock_title=MDTopAppBar(title='CLOCK',)
        self.clock_title.anchor_title = 'left'
        self.clock_title.left_action_items = [['menu']]
        self.clock_title.right_action_items = [['home',self.change_to_home]]
        self.clock_main.add_widget(self.clock_title)
        self.clock_item = BoxLayout(orientation = 'vertical')
        self.clock_item.add_widget(MDIconButton(icon='flower',pos_hint = {'center_x':0.5,'center_y':0.5}))
        self.clock_main.add_widget(self.clock_item)
        self.clock_screen.add_widget(self.clock_main)
    def work(self,*args):
        
        data =self.Entrybox.text
        files = 'abcdefghijklmnopqrstuvwxyz'
        file = ''
        for i in range(1,6):
            file += choice(files)
        generate_QRCODE(data,file+'.png')
        self.qrcode.source = file+'.png'
        self.filesa.append(file+'.png')
    def change_to_home(self,*args):
        self.root.transition = MDSlideTransition(direction= 'right')
        self.root.current = 'first'
    def save(self,*args):
        main =self.Entrybox.text
        generate_QRCODE(main,'QRCODE.png')
    def clock(self,*args):
        self.root.transition = MDSlideTransition(direction = 'left')
        self.root.current = 'clock'
    def on_stop(self):
        for file in self.filesa:
            os.remove(file)
        return super().on_stop()

if __name__ == '__main__':
    app = QRCODE()
    app.run()
   