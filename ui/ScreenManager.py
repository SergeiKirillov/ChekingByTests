from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.screens.setting import Setting
from ui.screens.theme import Theme
from ui.screens.mainScreen import MainScreen
from ui.screens.testing import Testing
from ui.screens.statictica import Statictic
from ui.screens.exsam import Exsam
from kivy.core.window import Window
from kivy.utils import platform
from data.config.constants import Constants
#from data.config.session import Session
from data.ApplicationContext import ApplicationContext




if platform in ("win", "linux"):
    Window.minimum_width = Constants.WINDOW_MIN_WIDTH
    Window.minimum_height = Constants.WINDOW_MIN_HEIGHT
    Window.resizable=True



class MyApp(App):
#    def __init__(self,session,**kwargs):
#        super().__init__(**kwargs)
#        self.session=session
    def __init__(self,context,**kwargs):
        super().__init__(**kwargs)
        self.context=context
        
    
    def build(self):
        sc=ScreenManager()

        sc.add_widget(Theme(name="theme")) # начинаем с выбора темы для
        sc.add_widget(MainScreen(name="login"))  #окно ввода табельного номера
        sc.add_widget(Setting(name="setting"))
        sc.add_widget(Testing(name="testing"))
        sc.add_widget(Exsam(name="exsam"))
        sc.add_widget(Statictic(name="statictic"))
    
        return sc
    
#MyApp().run()