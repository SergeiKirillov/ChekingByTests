import json
import os

from core.question import Question
from core.answer import Answer
from pathlib import Path

class QuestionLoader:
    @staticmethod
    def load(filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, filename)

        #data/questions.json"
        file_path = Path("data")/"questions.json"
        # Создаем директорию, если она не существует
        #file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # with open(filename, "r",encoding="utf-8") as f: #Windows
        with open(file_path, "r",encoding="utf-8") as f:
            data = json.load(f)
            
            """
            data - type - list
            data[0] - type - dict
            """
            
        questions=[]

        for item in data:
            answers = [
                Answer(a["text"], a["correct"])
                for a in item["answers"]
            ]
            questions.append(
                Question(
                    item["id"],
                    item["topic"],
                    item["question"],
                    answers,
                    item.get("comment", "")
                )
            )
        return questions
