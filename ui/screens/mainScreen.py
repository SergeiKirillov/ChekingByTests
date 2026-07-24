from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.screens.setting import Setting
from ui.screens.theme import Theme
from ui.screens.navigator import navigatorMenu
from kivy.metrics import dp, sp
from data.config.constants import Constants
from ui.screens.base_screen import BaseScreen


class MainScreen(BaseScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



        self.title.add_widget(
            Label(text="Введите табельной номер тестируемого работника", color="yellow", font_size=Constants.HEADER_HEIGHT*0.5)
        )
        blCenter=BoxLayout(orientation="vertical")
        
        anchorLogin=AnchorLayout(anchor_x = "center",anchor_y = "center")
        self.txtLoginName=TextInput(_hint_text="Введите табельный номер, и нажмите Enter", size_hint=(None, None), size=(500, 30),multiline=False)
        self.txtLoginName.input_filter = "int"  # Ограничение ввода только цифрами
        self.txtLoginName.bind(on_text_validate=self.on_enter_pressed) # type: ignore
        self.txtLoginName.bind(text=self.limit_length) # type: ignore # Ограничение длины ввода
        anchorLogin.add_widget(self.txtLoginName)
        
        self.lblLoginNameStatus = Label()
        self.lblLoginNameStatus.text=""
        self.lblLoginNameStatus.color="red"
        self.lblLoginNameStatus.font_size=Constants.HEADER_HEIGHT*0.3
        
        self.btnRegistrator = Button(text="Новый тестируемый", size_hint=(None,None), size=(200,50))
        self.btnRegistrator.opacity = 0
        self.btnRegistrator.disabled = True
        self.btnRegistrator.bind(on_press=self.btnRegistrator_click) # type: ignore
        anchorRegistrator=AnchorLayout(anchor_x = "center",anchor_y = "center")
        anchorRegistrator.add_widget(self.btnRegistrator)

        self.status.add_widget(self.lblLoginNameStatus)

        
        blCenter.add_widget(Widget())
        blCenter.add_widget(anchorLogin)
        blCenter.add_widget(anchorRegistrator)
        blCenter.add_widget(Widget())

        
        self.contentCenter.add_widget(blCenter)


#TODO: переход на другой экран
    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()  # type: ignore
        else:
            self.manager.current=screen


#    def btn_click(self, instance):  
#        #print(self.manager.current)
#        self.manager.current = "theme"

#TODO: Обработку нажатия Enter в TextInput поля ввода табельного номера
    def on_enter_pressed(self, instance):
        
        #[x]: Проверка на существование пользователя в userdb.load
        user = self.context.userdb.LoadUser(instance.text)
        if user is not None:
            self.lblLoginNameStatus.text=""
            self.btnRegistrator.opacity=0
            self.btnRegistrator.disabled=True
            self.context.session.user=user.name # Передаем имя пользователя из userdb в session
            #[ ]: Если тема найдена то возвращаем список, а если нет то пустой список
            checkQ=user.topics.get(self.context.session.theme, "Undefined")
            #if user.topics[self.context.session.theme] is not None:
            if checkQ != "Undefined":
                #self.context.session.questions = user.topics[self.context.session.theme]["question_stats"] # Передаем номера вопросов на которые были получены правильные ответы
                self.context.session.questions = checkQ["question_stats"]  # Передаем номера вопросов на которые были получены правильные ответы
            else:
                self.context.session.questions = []
            self.manager.current = "testing"

        else:
            self.lblLoginNameStatus.text="Нет такого пользователя"
            self.btnRegistrator.opacity=1
            self.btnRegistrator.disabled=False

         

#TODO:ограничение кол-ва вводимых знаков в проле ввода табельного номера
    def limit_length(self, instance, value):
        max_length = 8  # Максимальная длина ввода
        if len(value) > max_length:
            instance.text = value[:max_length]
#TODO: При нажатии на кнопку регистрации создаем файл с нулевыми данными
    def btnRegistrator_click(self, instance):
        self.context.userdb.createUser(self.txtLoginName.text)
        self.context.session.user=self.context.userdb.name
        print(self.context.session.user)
        self.context.session.questions = []
        self.manager.current = "testing" #Переходим на страницу тестирования



        
    

