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


class Theme(BaseScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

            

        #blThemeMain=BoxLayout(orientation="vertical")
        #blThemeTitle=BoxLayout(orientation="horizontal")
        #blThemeTitle.size_hint_y=None
        #blThemeTitle.height=Constants.HEADER_HEIGHT*0.5
        #blThemeSelect=BoxLayout(orientation="vertical")
        
        #lblTitle = Label(text="Выбор темы контрольных заданий", color="yellow",font_size=Constants.HEADER_HEIGHT*0.5)
        ##lblTitle.size_hint=(None,None)
        ##lblTitle.font_size=30
        #blThemeTitle.add_widget(lblTitle)

        #btnThemeElect = Button(text="Электробезопастность",size_hint=(None,None),size=(Constants.BUTTON_WIDTH,Constants.BUTTON_HEIGHT))
        #btnThemeElect.id="electr"
        #btnThemeElect.bind(on_release=self.btnThemeSelect_click)

        #btnThemeProm = Button(text="Промбезопастность",size_hint=(None,None),size=(Constants.BUTTON_WIDTH,Constants.BUTTON_HEIGHT))
        #btnThemeProm.id="Prombez"
        #btnThemeProm.bind(on_release=self.btnThemeSelect_click)

        
        #blThemeSelect.add_widget(Widget())
        #blThemeSelect.add_widget(btnThemeElect)
        #blThemeSelect.add_widget(btnThemeProm)
        #blThemeSelect.add_widget(Widget())
        #blThemeSelectWindows=BoxLayout(orientation="horizontal")
        #blThemeSelectWindows.add_widget(Widget())
        #blThemeSelectWindows.add_widget(blThemeSelect)
        #blThemeSelectWindows.add_widget(Widget())    

        #blThemeMain.add_widget(blThemeTitle)
        #blThemeMain.add_widget(blThemeSelectWindows)
        #blThemeMain.add_widget(navigatorMenu(self.change_screen))
       
        #self.add_widget(blThemeMain)

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
        self.manager.current="testing"            #Отображаем экран    

    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen