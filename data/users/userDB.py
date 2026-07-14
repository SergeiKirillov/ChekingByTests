import json
from pathlib import Path
from rich import print 
#from data.config.session import Session


class UserDB:
    def __init__(self, login=""):
        self.name = login
        self.total_tests=0
        self.total_questions=0
        self.total_correct=0
        self.total_wrong=0
        self.questions_per_session=1
        self.topics={}

    @classmethod
    def from_dict(cls, data):
        userDB = cls()
        userDB.name = data["name"]
        userDB.total_tests = data["total_tests"]
        userDB.total_questions = data["total_questions"]
        userDB.total_correct = data["total_correct"]
        userDB.total_wrong = data["total_wrong"]
        userDB.questions_per_session=data["questions_per_session"]
        userDB.topics=data["topics"]
        return userDB
    
    def to_dict(self):
        return {
            "login": self.name,
            "total_tests": self.total_tests,
            "total_questions": self.total_questions,
            "total_correct": self.total_correct,
            "total_wrong": self.total_wrong,
            "topics": self.topics
        }
    
    def LoadUser(self):
        try:
            #TODO: Если пользователь имеет 0 имя то выход
            if self.name=="":
              return 1
            else:
                try:
                    #FIXME: Нужно перевести ввод данных на context.database
                    self.context.database.load_user(userL)
                    file_path = Path("data")/ "users" / f"{self.name}.json"
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(file_path,"r",encoding="utf-8") as f:
                        #data = json.load(f)
                        return UserDB.from_dict(json.load(f))
                except FileNotFoundError:
                    #Файл или директория не найдены
                    return 3
        except Exception as e:
            #TODO: Добавить запись ошибки в лог файл 
            raise e

    def createUser(self):
        try:
            file_path = Path("data")/ "users" / f"{self.name}.json"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path,"w",encoding="utf-8") as file:
                json.dump(
                    self.to_dict(),
                    file,
                    ensure_ascii=False,
                    indent=4
                )
        except Exception as e:
            raise e
            

    def createUser0(self):
        try:
                

            user_data = {
                "name": self.name,
                "total_tests": 0,
                "total_questions": 0,
                "total_correct": 0,
                "total_wrong": 0,
                "questions_per_session": 10,
                "topics": {
                }
            }

            #file_name ="data/users/"+self.name+".json" 
            #with open(file_name,"w", encoding="utf-8") as file:
            file_path = Path("data")/ "users" / f"{self.name}.json"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path,"w",encoding="utf-8") as file:
                json.dump(
                    user_data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )
            #print(f"[bold yellow]Пользователь {self.name} создан[/bold yellow]")
            #print("[bold yellow]Войдите под именем нового пользователя.[/bold yellow]")
        except Exception as e:
            raise e
        
    def save_user(self, context, correct_questions):
        """
        name - имя пользователя

        correct_questions - список номеров вопросов,
        на которые пользователь ответил правильно
        """
        #TODO: db - получать или считывать из сессии, чтобы не передавать в метод

        try:
            
            #file_name = "data/users/"+ self.name +".json"
            #with open(file_name,"r", encoding="utf-8") as file:
            file_path = Path("data")/ "users" / f"{context.session.user}.json"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path,"r",encoding="utf-8") as file:
                user_data = json.load(file)
            #print(type(user_data))
            #print(type(correct_questions))
            #Ищем ключь равный имени файла теста
            
            if context.session.theme in user_data['topics']:
                #Если найден то добавляем в [ключ][ключ] список правильных ответов
                ...
                # Добавляем новые вопросы, избегая дубликатов
                current_questions = set(user_data['topics'][context.session.theme]['question_stats'])
                for qid in correct_questions:
                    current_questions.add(qid)
                user_data['topics'][context.session.theme]["question_stats"]=sorted(list(current_questions))

            else:
                #сортируем по возрастанию
                correct_questions_sorted = sorted(list(correct_questions))
                #Если ключ не найден, то добавляем всю секцию
                user_data["topics"][context.session.theme]={
                    "questions_per_session": 10,
                    "question_stats": correct_questions_sorted
                }   
            
            #print(user_data)    
            
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(
                    user_data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )
        except Exception as e:
            raise e
