from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.screens.navigator import navigatorMenu
from kivy.metrics import dp,sp
from data.config.constants import Constants


class Statictic(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        blStatisticMain=BoxLayout(orientation="vertical")
        blStatisticSelect=BoxLayout(orientation="vertical")
        
        lblStatisticTitle=Label(text="Экрон статистик", color="yellow")
        lblStatisticTitle.font_size=Constants.HEADER_HEIGHT*0.5
        blStatisticSelect.add_widget(lblStatisticTitle) 
        
        blStatisticMain.add_widget(blStatisticSelect)
        blStatisticMain.add_widget(navigatorMenu(self.change_screen))
        
        self.add_widget(blStatisticMain)

    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen    

            