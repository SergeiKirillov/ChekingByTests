import json
from pathlib import Path
from rich import print 
#from data.config.session import Session

class User:
    def __init__(self, context):
        self.name = context.session.user
        self.context=context
        
    def LoadUser(self):
        try:
            #nameUser ="data/users/"+self.name+".json" 
            file_path = Path("data")/ "users" / f"{self.name}.json"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path,"r",encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            #print("Пользователь не найден")
            return None
        except Exception as e:
            raise e
        else:
            return False
            pass


    def createUser(self):
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


class User0:
    def __init__(self, context):
        self.name = context.session.user
        self.context=context
        
    def LoadUser(self):
        try:
            #nameUser ="data/users/"+self.name+".json" 
            file_path = Path("data")/ "users" / f"{self.name}.json"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path,"r",encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            #print("Пользователь не найден")
            return None
        except Exception as e:
            raise e
        else:
            return False
            pass


    def createUser(self):
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
