from kivy.app import App
from kivy.uix import label
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.screens.navigator import navigatorMenu
from kivy.metrics import dp,sp
from data.config.constants import Constants
from ui.screens.base_screen import BaseScreen



class Statictic(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        lblStatisticTitle=Label(text="Экран статистики", color="yellow")
        lblStatisticTitle.font_size=Constants.HEADER_HEIGHT*0.5
        self.title.add_widget(lblStatisticTitle)

        self.lblStatisticName = Label(text="Пользователь: " , color="white")
        self.lblStatisticName.font_size=Constants.HEADER_HEIGHT*0.3
        self.lblStaticticThemeName = Label(text="Тема вопросов: ", color="white")
        self.lblStaticticThemeName.font_size=Constants.HEADER_HEIGHT*0.3
        self.lblStaticticQuestionCount = Label(text="Кол-во вопросов: ", color="white")
        self.lblStaticticQuestionCount.font_size=Constants.HEADER_HEIGHT*0.3
        self.lblStaticticQuestionCountOK = Label(text="Кол-во правильных ответов: ", color="green")
        self.lblStaticticQuestionCountOK.font_size=Constants.HEADER_HEIGHT*0.3
        self.lblStaticticQuestionCountNotOK = Label(text="Кол-во НЕ правильных ответов: ", color="red")
        self.lblStaticticQuestionCountNotOK.font_size=Constants.HEADER_HEIGHT*0.3

        self.contentCenter.add_widget(self.lblStatisticName)
        self.contentCenter.add_widget(self.lblStaticticThemeName)
        self.contentCenter.add_widget(self.lblStaticticQuestionCount)
        self.contentCenter.add_widget(self.lblStaticticQuestionCountOK)
        self.contentCenter.add_widget(self.lblStaticticQuestionCountNotOK)



    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen

    def on_pre_enter(self):
        self.lblStatisticName.text=self.lblStatisticName.text+self.context.session.user
        self.lblStaticticThemeName.text=self.lblStaticticThemeName.text+self.context.session.topic
        self.lblStaticticQuestionCount.text=self.lblStaticticQuestionCount.text+str(self.context.session.ask_count)
        self.lblStaticticQuestionCountOK.text=self.lblStaticticQuestionCountOK.text+str(self.context.session.ask_OK_count)
        self.lblStaticticQuestionCountNotOK.text=self.lblStaticticQuestionCountNotOK.text+str(self.context.session.ask_noOK_count)