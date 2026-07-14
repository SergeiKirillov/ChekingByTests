import argparse
#from data.config.session import Session
from data.ApplicationContext import ApplicationContext

def parse_args():
    parser = argparse.ArgumentParser(
        description="Система проверки знаний"
    )
    parser.add_argument(
        "--ui",
        choices=["terminal", "rich", "kivy"], 
        default="terminal",
        help="Тип интерфейса"
    )
    parser.add_argument(
        "--theme",
        default=None,
        help="Тема вопросов"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    
    
    #Создаём Session один раз
    #session = Session()
    app_context = ApplicationContext()

    if (args.ui=="rich" or args.ui=="terminal"):
        #from ui.terminal_ui import TerminalUI
        #from ui.rich_ui import RichUI
        from core.application import Application
        #app = Application(session, ui_type = args.ui , theme=args.theme)
        #app().selectDB()
        #app.run("electrical")
        #Application(session, ui_type = args.ui , theme=args.theme).selectDB()
        app_context.session.theme=args.theme #используем сессию
        app_context.session.ui=args.ui #используем сессию
        Application(app_context).selectDB()    
    elif args.ui=="kivy":
        import os
        os.environ["KIVY_NO_ARGS"] = "1"
        from ui.ScreenManager import MyApp
        #MyApp(session).run() #Session передаём через контекст
        MyApp(app_context).run() #Session передаём через контекст

if __name__=="__main__":
    main()    
    

