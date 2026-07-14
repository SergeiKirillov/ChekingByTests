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
        btnMain=Button(text="Главный экран")
        btnMain.size=(btnMain.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnMain.texture_update()
        btnMain.bind(on_press=lambda x: callback("main")) # type: ignore

        #btnSelectTheme=Button(text="Выбор темы",size_hint_x=None,width=110)
        btnSelectTheme=Button(text="Выбор темы")
        btnSelectTheme.size=(btnMain.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnSelectTheme.disabled=False
        btnSelectTheme.texture_update()
        btnSelectTheme.bind(on_press=lambda x: callback("theme")) # type: ignore

        #btnTest=Button(text="Тестирование",size_hint_x=None,width=110)
        btnTest=Button(text="Тестирование")
        btnTest.size=(btnMain.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnTest.disabled=True
        btnTest.texture_update()
        btnTest.bind(on_press=lambda x: callback("testing")) # type: ignore

        #@btnExam=Button(text="Экзаменирование",size_hint_x=None,width=110)
        btnExam=Button(text="Экзаменирование")
        btnExam.size=(btnMain.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnExam.disabled=True
        btnExam.texture_update()    
        btnExam.bind(on_press=lambda x: callback("exsam")) # type: ignore

        #btnStat=Button(text="Статистика",size_hint_x=None,width=110)
        btnStat=Button(text="Статистика")
        btnStat.size=(btnMain.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnStat.disabled=True
        btnStat.texture_update()
        btnStat.bind(on_press=lambda x: callback("statictic")) # type: ignore

        #btnSetting=Button(text="Настройка",size_hint_x=None,width=110)
        btnSetting=Button(text="Настройка")
        btnSetting.size=(btnMain.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnSetting.disabled=True
        btnSetting.texture_update()
        btnSetting.bind(on_press=lambda x: callback("setting")) # type: ignore
 
        #btnExit=Button(text="Выход",size_hint_x=None,width=110)
        btnExit=Button(text="Выход")
        btnExit.size=(btnMain.texture_size[0]+20,Constants.NAV_HEIGHT)
        btnExit.texture_update()
        btnExit.bind(on_press=lambda x: callback("exit")) # type: ignore

        self.add_widget(btnMain)
        self.add_widget(btnSelectTheme)
        self.add_widget(btnTest)
        self.add_widget(btnExam)
        self.add_widget(btnStat)
        self.add_widget(btnSetting)
        self.add_widget(btnExit)

    def click_exit(self, instance):
        #App.get_running_app().stop()
        pass

    

    