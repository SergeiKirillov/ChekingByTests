from data.users.user import User
from data.users.userDB import UserDB
from core.question_db import QuestionDB
from core.question_db import Question_v2
from core.testing import Testing
from core.testManager import TestManager
from pathlib import Path



class Application:

    #def __init__(self, session, ui_type="terminal", theme=None):
    def __init__(self, context):
        self.context = context
        
        if self.context.session.ui == "rich":
            from ui.rich_ui import RichUI
            self.ui = RichUI()
        else:
            from ui.terminal_ui import TerminalUI
            self.ui = TerminalUI()
        
        #self.current_user = None
        #self.fileJSONdescript = None #Имя теста для вывода на экран
        #self.selected_test=None  #имя файла выбранных тестов
        
    
    
    def login(self, nameLog=""):
        userText=""
        if nameLog=="":
            userL=(self.ui.ask_input("Введите имя пользователя > ")).replace(" ", "")
            #user = self.context.database.load_user(userL)
            self.context.userdb.name=userL
            user = self.context.userdb.LoadUser()
            if user is not None:
                userText=user["name"] 
            else :
                self.ui.show_message("Пользователя не существует")
                self.registration(userL)
        else:
            userText = nameLog
        
        self.context.session.user=userText 
        self.run()
        
            

    def registration(self, nameLog=""):
        
        loginNum:str=""

        if nameLog == "":
            loginNum=self.ui.ask_input("Введите имя нового пользователя > ").replace(" ", "")
            self.registration(loginNum)
        else:
            if (self.ui.ask_input(f"Вы хотите добавить нового пользователя ({nameLog}) > (Y/N)")).upper() == "Y":
                loginNum = nameLog

            else:
                self.registration()
                exit()


        data={
            "name": loginNum,
            "total_tests": 0,
            "total_questions": 0,
            "total_correct": 0,
            "total_wrong": 0,
            "questions_per_session": 10,
            "topics": {}
        }
        dataNewuser = self.context.database.save_user(loginNum,data)
        self.login(loginNum)
        
        
    def testing1007(self):


        #TODO: Модуль тестирования переделать

        #[x]: ---------=Загружаем настройки пользователя  =-----------------------------------------
        # используем session для передачи параметров 
        # self.context.userdb.name - имя пользователя в базе 
        # self.context.session.user - имя пользователя в сессии
        # numbers_OK_number - переменная в которую из файла пользователя мы передаём список вопросов на который получен положительный ответ 
        # countAns - кол-во вопросв при тестировании

        self.context.userdb.name=self.context.session.user
        self.context.userdb=self.context.userdb.LoadUser()
        countAns =self.context.userdb.questions_per_session #кол-во вопросв при тестировании
        numbers_OK_number = self.context.userdb.topics["electrical"]["question_stats"]

        ##userSetting = user.LoadUser()  
        userSetting = {}

        #Если настроек нет то выходим  
        if userSetting is None:
            raise SystemExit
        else:
            
            #Загружаем все вопросы из файла в переменную в виде словаря
            db=self.context.database.load_test(self.context.session.theme)

            ans = Testing(numbers_OK_number) #Передаем номера вопросов на которые уже успешно отвечали
           
            number_god_session=[]
           
            # Цикл вопросов от 0 до максимального кол-ва вопрсосов за секцию
            for ask in range(countAns):
                #генерируем случайное число из избранного списка за исключением вопросов на которые ранее были получены положительные ответы  
                answers_number = ans.rand_ans()


#[x]: Используем клас QuestionDB для формирования вопросов, перемешивания ответов и вывод в Session               
                ##dbTest = QuestionDB(self.context.session.theme)
                ##question = dbTest.get_question(answers_number)
                
                #question0 = self.context.database.get_question(answers_number,db) #Получаем выбранный вопрос в виде словаря 
                #question=Question_v2(question0) #Переводим словарь в переменные класса
                
                question=Question_v2(self.context.database.get_question(answers_number,db)) #Переводим словарь в переменные класса
                # question.id - номер вопроса
                # question.question - вопрос
                # question.comment - комментарий


                #print(type(question))
                if question:
                    ## обновляем экран с вопросом
                    
                    question_id = question.id
                    question_text=question.question
                    answers=question.answers
                    quest_number_user=self.ui.show_question(ask, countAns, question_id, question_text, answers)
                          
                    if question.check_answer(quest_number_user):
                        #если ответ правильный
                        self.ui.success("Правильно")
                        #если правильно то добавляем в список этот вопрос 
                        number_god_session.append(answers_number)
                    else:
                        self.ui.error("Не Правильно")
                        self.ui.show_message(f"Правильный ответ: {question.get_correct_answer()}")
                    self.ui.pause()

            #блок записи в статистику правильных ответов     
            #список номеров вопросов на которые был получен правильные ответы

            self.ui.show_message(f"Кол- во вопросов {countAns}, кол-во правильных ответов {len(number_god_session)}")
            full_ans=number_god_session
            self.context.database.save_user(self.context.session.user, self.context.session.theme, number_god_session)
            


            self.ui.pause()
        



    def learning(self):
        ...

    def settings(self):
        ...

    def guest_menu(self):
        choice = self.ui.show_menu(
                    "Главное меню",
                    [
                        "Выход",
                        "Вход",
                        "Регистрация"
                    ]
                )
        match choice:
            case 1:
                self.login()
            case 2:
                self.registration()
            case 0:
                raise SystemExit
    
    def user_menu(self):
        choice = self.ui.show_menu(
                    f"Выбран пользователь: {self.context.session.user}",
                    [
                        "Выход",
                        "Тестирование",
                        "Проверка знаний",
                        "Настройки",
                        "Выход из учётной записи"             
                    ]
                )
        match choice:
            case 1:
                self.testing1007()
            case 2:
                self.learning()
            case 3:
                self.settings()
            case 4:
                self.current_user=None
            case 0:
                raise SystemExit

    def selectDB(self):
        manager = TestManager(self.context)
        tests = manager.get_tests_names()
        choice = self.ui.show_menu("Выбор тестов",tests)
        #self.selected_test = 
        self.context.session.theme = tests[choice]
        
        #self.run(self.selected_test)
        self.run()

    def loadDB(self):
        try:
            manager = TestManager(self.context)
            selectDBload = manager.load_test()
            self.context.session.topic = selectDBload["title"]
            return selectDBload
        except Exception as e:
            raise e
        
    

    def run(self):
        # Проверка что файл существует
        if self.context.session.theme != "":
            db = self.loadDB()
#            self.selected_test=nameDb # сохраняем выбранную тему в переменные класса  
        else:
            self.ui.error("База не найдена")   
            raise SystemExit

#            self.ui.show_message(db["title"])
        self.ui.show_message(self.context.session.topic)
        while True:
            if self.context.session.user == "":
                self.guest_menu()
            else:
                self.user_menu()
    
    def testing(self):
        #TODO: Модуль тестирования переделать
        # Загружаем настройки пользователя  
        userName = self.context.session.user
        #user = self.context.database.load_user(userL)
        user = User(self.context) 
        userSetting = user.LoadUser()

        #Если настроек нет то выходим  
        if userSetting is None:
            raise SystemExit
        else:
            #Загружаем вопросы
            #selDB = Path("data")/ "tests" / f"{self.selected_test}.json"
            selDB = Path("data")/ "tests" / f"{self.context.session.theme}.json"
            db=QuestionDB(selDB)
            
            
            number_god_session=[]
            #question_stats - ключ словаря где храниться список вопросов на которые успешно ответили
            #questions_per_session - кол-во вопросов провекрки за секцию
            #numbers_god_number - переменная в которую мы передаём список вопросов 
            #numbers_god_number=userSetting["question_stats"]
            numbers_god_number=[]
            if self.context.session.theme in userSetting["topics"]:
               # print(userSetting)
                numbers_god_number=userSetting["topics"][self.context.session.theme]["question_stats"]
            

            #try:
                #необходимо указать путь в хранилице где будут храниться пройденные вопросы 
                #numbers_god_number=userSetting["question_stats"] 
            #except KeyError as e:
                #Если нет такой секции то считаем что это первый запуск этого теста
            #    numbers_god_number=[]
            
            
            countAns =userSetting["questions_per_session"] #кол-во вопросв при тестировании
            ans = Testing(numbers_god_number) #Передаем номера вопросов  

            # Цикл вопросов от 0 до максимального кол-ва вопрсосов за секцию
            for ask in range(countAns):
                #генерируем случайное число из избранного списка за исключением вопросов на которые ранее были получены положительные ответы  
                answers_number = ans.rand_ans()

                #достаем Заданный вопрос    
                question = db.get_question(answers_number) 
                
                #print(type(question))
                if question:
                    #current_question_text = f"Вопрос {ask + 1}/{countAns}"
                    ## обновляем экран с вопросом
                    #self.ui.show_question(current_question_text)
                    #self.ui.show_question(question.show())
                    
                    #self.ui.show_message(question.id)
                    #self.ui.show_message(question.question)
                    #self.ui.show_message(question.answers)
                    
                    question_id = question.id
                    question_text=question.question
                    #answers=question.show() #возвращает строку
                    answers=question.answers
                    #print(answers)
                    quest_number_user=self.ui.show_question(ask, countAns, question_id, question_text, answers)

                   
                                             
                    if question.check_answer(quest_number_user):
                        #если ответ правильный
                        self.ui.success("Правильно")
                        #если правильно то добавляем в список этот вопрос 
                        number_god_session.append(answers_number)
                    else:
                        self.ui.error("Не Правильно")
                        self.ui.show_message(f"Правильный ответ: {question.get_correct_answer()}")

                    self.ui.pause()

            #блок записи в статистику правильных ответов     
            #список номеров вопросов на которые был получен правильные ответы

            self.ui.show_message(f"Кол- во вопросов {countAns}, кол-во правильных ответов {len(number_god_session)}")
            full_ans=number_god_session
            user.save_user(self.context,full_ans)


            self.ui.pause()
        