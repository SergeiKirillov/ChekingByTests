from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.screenmanager import ScreenManager, Screen
from data.ApplicationContext import ApplicationContext
from data.config.constants import Constants
from ui.screens.navigator import navigatorMenu

class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.root_layout = BoxLayout(orientation="vertical")
        
        #self.title = BoxLayout(orientation="horizontal", size_hint_y=None, height=50)
        self.title = AnchorLayout(anchor_x = "center",anchor_y = "center",size_hint_y=None,height=Constants.HEADER_HEIGHT)
        
        #TODO: элемент Статус на базовом экране
        self.status = BoxLayout(orientation="horizontal", size_hint_y=None, height=30)
        #TODO: Элемент основной контент на базовом экране
        self.content = BoxLayout()
        self.contentRight=BoxLayout(orientation="vertical")
        self.contentLeft=BoxLayout(orientation="vertical")
        self.contentCenter=BoxLayout(orientation="vertical")
        self.content.add_widget(self.contentLeft)
        self.content.add_widget(self.contentCenter)
        self.content.add_widget(self.contentRight)
        #TODO: Элемент кнопки навигации на базовом экране
        self.navigation = navigatorMenu(self.change_screen)
        self.root_layout.add_widget(self.title)
        self.root_layout.add_widget(self.status)
        self.root_layout.add_widget(self.content)
        self.root_layout.add_widget(self.navigation)
        self.add_widget(self.root_layout)
    
    @property
    def context(self):
        #FIXME: Что должно быть за место context
        return App.get_running_app().context
    
    @property
    def context2(self):
        return App.get_running_app().context2
        
    
    @property
    def database(self):
        return self.context.database
    @property
    def session(self):
        return self.context.session
    @property
    def userdb(self):
        return self.context.userdb
    
    def goto(self, screen):
        self.manager.current = screen
        
        
    