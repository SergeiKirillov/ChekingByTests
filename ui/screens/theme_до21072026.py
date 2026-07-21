from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from ui.screens.setting import Setting
from ui.screens.navigator import navigatorMenu
from kivy.uix.widget import Widget
from data.config.constants import Constants
from ui.screens.base_screen import BaseScreen
from core.testManager import TestManager


class Theme(BaseScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

       

        #TODO: на экране выбора темы опроса переделываем под base_screen
        self.title.add_widget(
            Label(text="Выберите тему для тестирования", color="yellow", font_size=Constants.HEADER_HEIGHT*0.5)
        )
        
        btnThemeElect = Button(text="Электробезопастность",size_hint=(None,None),size=(Constants.BUTTON_WIDTH,Constants.BUTTON_HEIGHT))
        btnThemeElect.id="electr"
        btnThemeElect.bind(on_release=self.btnThemeSelect_click)
        btnThemeProm = Button(text="Промбезопастность",size_hint=(None,None),size=(Constants.BUTTON_WIDTH,Constants.BUTTON_HEIGHT))
        btnThemeProm.id="Prombez"
        btnThemeProm.bind(on_release=self.btnThemeSelect_click)
        blThemeButton=BoxLayout(orientation="vertical")
        blThemeButton.add_widget(Widget())
        blThemeButton.add_widget(btnThemeElect)
        blThemeButton.add_widget(btnThemeProm)
        blThemeButton.add_widget(Widget())
        contentCenterAnchor=AnchorLayout(anchor_x = "center",anchor_y = "center")
        contentCenterAnchor.add_widget(blThemeButton)
        self.contentCenter.add_widget(contentCenterAnchor)
    


    def btnThemeSelect_click(self, instance):
        if instance.id=="electr":
            screen=self.manager.get_screen("testing") #Получаем доступ к экрану
            #screen.test_name="Электробезопастность"   #Присваиваем переменной этого экрана значение 
            #screen.data={"topic":"Электробезопастность","questions":10,"user":"019261"}
            self.session.topic="Электробезопастность"
            self.session.theme="electr"
        elif instance.id=="Prombez":
            screen=self.manager.get_screen("testing")
            #screen.test_name="Промбезопастность"
            #screen.data={"topic":"Промбезопастность","questions":10,"user":"019261"}
            self.session.topic="Промбезопастность"
            self.session.theme="Prombez"
        
        #print(self.context.session.theme)
        #print(self.context.session.topic)

        self.manager.current="testing"            #Отображаем экран    

    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen

    def on_pre_enter(self, *args):
        pass

    def button_create(self,content):
        tests=TestManager(content).load_tests()
        for test in tests:
            btn=Button(
                text=test.name,
                size_hint_y=None,
                height =50
            )
            btn.test=test
