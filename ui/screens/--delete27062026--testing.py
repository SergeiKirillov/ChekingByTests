from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.screens.navigator import navigatorMenu
from kivy.metrics import dp,sp
from kivy.clock import Clock
from data.config.constants import Constants
from ui.screens.base_screen import BaseScreen

from core.testManager import TestManager


class Testing(BaseScreen):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.test_name=""
        self.data={}
        blTestingMain=BoxLayout(orientation="vertical")
        
        self.blTestingQuestion=BoxLayout(orientation="vertical")
        self.blTestingStatistic=BoxLayout(orientation="horizontal")
        
        self.lblTitle = Label(text="Тестирование", color="yellow")
        self.lblTitle.font_size = Constants.HEADER_HEIGHT*0.5
        self.title.add_widget(self.lblTitle)

        # self.blTestingQuestion.clear_widgets()
        self.lblAsk = Label(text="", color="white")
        self.lblAsk.font_size = Constants.HEADER_HEIGHT * 0.35
        self.lblAsk.text_size = (Constants.LABEL_TEXT_SIZE, None)
        self.lblAsk.halign = "center"
        self.lblAsk.valign = "middle"
        



        
        blTestingMain.add_widget(self.blTestingQuestion)
        blTestingMain.add_widget(self.blTestingStatistic)
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
        self.load_question()

    def load_question(self):

#[x]: Статистика ответов на вопрос. 
        statistic_text = "Вопрос: "+str(self.context.session.ask_count+1)+"/"+str(self.context.session.question_count) 
        statistic_OK_noOK = "+"+str(self.context.session.ask_OK_count)+"/ -"+str(self.context.session.ask_noOK_count)
        self.lblStatistic=Label(text=str(statistic_text+" "+statistic_OK_noOK), color="blue")
        self.lblStatistic.font_size = Constants.HEADER_HEIGHT * 0.35
        self.lblStatistic.text_size = (Constants.LABEL_TEXT_SIZE, None)
        self.lblStatistic.halign = "center"
        self.lblStatistic.valign = "middle"
        #self.blTestingStatistic.add_widget(self.lblStatistic)
        self.status.add_widget(self.lblStatistic)

        

# Получаем номер вопроса для тестирования которого нет в списке правильных ответов
        number = self.context.session.rand_ans()
        self.context.session.get_answer(number)
# Загружаем вопрос на экран
        self.lblAsk.text=self.context.session.question
        self.lblAsk.text_size = (self.lblAsk.width, None)
        self.lblAsk.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.lblAsk.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.lblAsk.size_hint_y = None
        self.blTestingQuestion.add_widget(self.lblAsk)

# Загружаем ответы на экран
        self.answer_buttons=[]
        for i, answer in enumerate(self.context.session.answers):
            btn = Button(text=answer["text"])
            #btn.text_size=(Constants.LABEL_TEXT_SIZE,None)
            #btn.halign = "center"
            #btn.valign = "middle"
            btn.size_hint_y=None
            btn.bind(width=lambda instance, value: setattr(instance, 'text_size', (value - 20, None)))
            btn.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1] + 20))
            btn.bind(on_release=lambda btn, index=i: self.on_answer(index))
            self.answer_buttons.append(btn)
            self.blTestingQuestion.add_widget(btn)


    def on_answer(self, index):
        # смотрим какое значение у поля correct ответа под номером index, если true то правильный ответ
        btn = self.answer_buttons[index]

        if self.context.session.checking_answer(index):
           btn.background_color=(0,1,0,1)   
        else:
           self.answer_buttons[self.context.session.ask_OK_index].background_color=(0,1,0,1)
           btn.background_color=(1,0,0,1)
        btn.disabled = True

        Clock.schedule_once(self.show_next_question,2)        

#Следующий вопрос
    def show_next_question(self, dt):
#[x]: Цикл обратного отсчёта. Максимальное кол-во вопросов
        if (self.context.session.ask_count<self.context.session.question_count):
            self.reset_screen()
            self.load_question()
        else:
#[ ]: Сохранение данных в файл после окончания тестирования 
            self.manager.current = "statictic"
#Очистка экрана
    def reset_screen(self):
        self.blTestingQuestion.clear_widgets()  
        #self.blTestingStatistic.clear_widgets()

        self.status.clear_widgets()




#[FIXME]: Переделать интерфейс под базовый экран
#[FIXME]: Проверить ответ на первый вопрос
