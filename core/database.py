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
    
    def save_user(self, login, data):
        filename=(self.users/f"{login}.json")
        return self.save_json(filename, data)    

    def load_test(self, topic):
        filename = (self.tests / f"{topic}.json")
        return self.load_json(filename)
    
    def get_question(self, question_id, db):
        for q in db["questions"]:
            if q["id"]==question_id:
                return q #Question_v2(q)
        return None
    
