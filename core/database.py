import json
from pathlib import Path

class Database:
    def __init__(self):
        #self.data_dir = Path("data")
        self.root = Path("data")
        self.config = self.root / "config.json"
        self.users = self.root / "users"
        self.tests = self.root / "tests"

    def load_json(self, filename)->dict:
        if not filename.exists():
            return {}

        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def save_json(self, filename,  data):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )
    def load_config(self):
        return self.load_json(self.config)
    
    def save_config(self, config):
        self.save_json(self.config ,config)
    
    def load_user(self, login):
        filename=(self.users/f"{login}.json")
        return self.load_json(filename)
    
    def create_user(self, login, data):
        filename=(self.users/f"{login}.json")
        return self.save_json(filename, data)
    
    def save_user(self, login, theme, correct_questions):
        """
        name - имя пользователя

        correct_questions - список номеров вопросов,
        на которые пользователь ответил правильно
        """
        #TODO: db - получать или считывать из сессии, чтобы не передавать в метод
        
        try:
            filename=(self.users/f"{login}.json")
            user_data = self.load_json(filename)

#            #Ищем ключь равный имени файла теста
            
            if theme in user_data['topics']:
                #Если найден то добавляем в [ключ][ключ] список правильных ответов
                ...
                # Добавляем новые вопросы, избегая дубликатов
                current_questions = set(user_data['topics'][theme]['question_stats'])
                for qid in correct_questions:
                    current_questions.add(qid)
                user_data['topics'][theme]["question_stats"]=sorted(list(current_questions))

            else:
                #сортируем по возрастанию
                correct_questions_sorted = sorted(list(correct_questions))
                #Если ключ не найден, то добавляем всю секцию
                user_data["topics"][theme]={
                    "questions_per_session": 10,
                    "question_stats": correct_questions_sorted
                }   
            

            filename=(self.users/f"{login}.json")
            self.save_json(filename, user_data)    
        
        except Exception as e:
            raise e



    def load_test(self, topic):
        filename = (self.tests / f"{topic}.json")
        return self.load_json(filename)
    
    def get_question(self, question_id, db):
        for q in db["questions"]:
            if q["id"]==question_id:
                return q #Question_v2(q)
        return None
    
