from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.screens.navigator import navigatorMenu
from kivy.metrics import dp,sp
from data.config.constants import Constants
from ui.screens.base_screen import BaseScreen

from core.testManager import TestManager


class Testing(BaseScreen):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.test_name=""
        self.data={}
        blTestingMain=BoxLayout(orientation="vertical")
        blTestingTitle=BoxLayout(orientation="horizontal")
        blTestingQuestion=BoxLayout(orientation="vertical")
        blTestingStatistic=BoxLayout(orientation="horizontal")
        
        self.lblTitle = Label(text="Тестирование", color="yellow")
        self.lblTitle.font_size = Constants.HEADER_HEIGHT*0.5
        blTestingTitle.add_widget(self.lblTitle)

        blTestingMain.add_widget(blTestingTitle)
        blTestingMain.add_widget(blTestingQuestion)
        blTestingMain.add_widget(blTestingStatistic)
        blTestingMain.add_widget(navigatorMenu(self.change_screen))
        self.add_widget(blTestingMain)

    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen

    def on_enter(self):   #событие при открывании экрана,интерфейс ещё старый
        #self.lblTitle.text=self.test_name #Изменяем значение текстового поля.
        #self.lblTitle.text=self.data["topic"]
        txtTitle=self.session.topic
        self.lblTitle.text=txtTitle



