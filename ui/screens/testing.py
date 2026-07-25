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
        self.blTestingQuestion=BoxLayout(orientation="vertical")
        blTestingStatistic=BoxLayout(orientation="horizontal")
        
        self.lblTitle = Label(text="Тестирование", color="yellow")
        self.lblTitle.font_size = Constants.HEADER_HEIGHT*0.5
        blTestingTitle.add_widget(self.lblTitle)

        # self.blTestingQuestion.clear_widgets()
        self.lblAsk = Label(text="", color="white")
        self.lblAsk.font_size = Constants.HEADER_HEIGHT * 0.35
        self.lblAsk.text_size = (Constants.LABEL_TEXT_SIZE, None)
        self.lblAsk.halign = "center"
        self.lblAsk.valign = "middle"
        self.blTestingQuestion.add_widget(self.lblAsk)



        blTestingMain.add_widget(blTestingTitle)
        blTestingMain.add_widget(self.blTestingQuestion)
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


    def on_pre_enter(self):
        # Получаем номер вопроса для тестирования которого нет в списке правильных ответов
        number = self.context.session.rand_ans()
        self.context.session.get_answer(number)
        self.lblAsk.text=self.context.session.question

        # Получаем данные по этому вопросу

        for i, answer in enumerate(self.context.session.answers):
            btn = Button(text=answer["text"])
            btn.text_size=(Constants.LABEL_TEXT_SIZE,None)
            btn.halign = "center"
            btn.valign = "middle"
            btn.bind(on_release=lambda btn, index=i: self.on_answer(index))
            self.blTestingQuestion.add_widget(btn)


    def on_answer(self, index):
        # смотрим какое значение у поля correct ответа под номером index, если true то правильный ответ
        intAns = self.context.session.answers[index]["text"]
        blAns = self.context.session.answers[index]["correct"]
        if self.context.session.answers[index]["correct"]:
            print("Ответ правильный")
        else:
            print("Ответ не правильный")


