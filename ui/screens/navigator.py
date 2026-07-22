from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp,sp
from data.config.constants import Constants


class navigatorMenu(BoxLayout):

    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation="horizontal"
        self.size_hint_y=None
        self.height=Constants.NAV_HEIGHT

        #btnMain=Button(text="Главный экран",size_hint_x=None,width=110)
        btnLogin=Button(text="Таб номер")
        btnLogin.size=(btnLogin.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnLogin.texture_update()
        btnLogin.bind(on_press=lambda x: callback("login")) # type: ignore

        #btnSelectTheme=Button(text="Выбор темы",size_hint_x=None,width=110)
        btnSelectTheme=Button(text="Выбор темы")
        btnSelectTheme.size=(btnSelectTheme.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnSelectTheme.disabled=False
        btnSelectTheme.texture_update()
        btnSelectTheme.bind(on_press=lambda x: callback("theme")) # type: ignore

        #btnTest=Button(text="Тестирование",size_hint_x=None,width=110)
        btnTest=Button(text="Тестирование")
        btnTest.size=(btnTest.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnTest.disabled=True
        btnTest.texture_update()
        btnTest.bind(on_press=lambda x: callback("testing")) # type: ignore

        #@btnExam=Button(text="Экзаменирование",size_hint_x=None,width=110)
        btnExam=Button(text="Экзаменирование")
        btnExam.size=(btnExam.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnExam.disabled=True
        btnExam.texture_update()    
        btnExam.bind(on_press=lambda x: callback("exsam")) # type: ignore

        #btnStat=Button(text="Статистика",size_hint_x=None,width=110)
        btnStat=Button(text="Статистика")
        btnStat.size=(btnStat.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnStat.disabled=True
        btnStat.texture_update()
        btnStat.bind(on_press=lambda x: callback("statictic")) # type: ignore

        #btnSetting=Button(text="Настройка",size_hint_x=None,width=110)
        btnSetting=Button(text="Настройка")
        btnSetting.size=(btnSetting.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnSetting.disabled=True
        btnSetting.texture_update()
        btnSetting.bind(on_press=lambda x: callback("setting")) # type: ignore
 
        #btnExit=Button(text="Выход",size_hint_x=None,width=110)
        btnExit=Button(text="Выход")
        btnExit.size=(btnExit.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnExit.texture_update()
        btnExit.bind(on_press=lambda x: callback("exit")) # type: ignore


        self.add_widget(btnSelectTheme)
        self.add_widget(btnLogin)
        self.add_widget(btnTest)
        self.add_widget(btnExam)
        self.add_widget(btnStat)
        self.add_widget(btnSetting)
        self.add_widget(btnExit)

    def click_exit(self, instance):
        #App.get_running_app().stop()
        pass

    

    