from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.screens.navigator import navigatorMenu
from kivy.metrics import dp, sp
from data.config.constants import Constants


class Setting(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        blSettingMain=BoxLayout(orientation="vertical")
        blSettingSelect=BoxLayout(orientation="vertical")
        
        lblTitle=Label(text="Экрон настроек", color="yellow")
        lblTitle.font_size=Constants.HEADER_HEIGHT
        lblTitle.color="red"
        #btnMenu = Button(text="Назад в Меню",size_hint=(None, None),size=(200,20))
        blSettingSelect.add_widget(lblTitle)
        #blSettingSelect.add_widget(btnMenu)
        
        blSettingMain.add_widget(blSettingSelect)
        blSettingMain.add_widget(navigatorMenu(self.change_screen))

        
        self.add_widget(blSettingMain)

    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen
