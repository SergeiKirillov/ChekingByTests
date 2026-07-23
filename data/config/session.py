
class Session:
    def __init__(self):
        self.user:str = ""
        self.questions = [] #список правильных ответов
        self.questions_index:int = 0
        self.correct:int = 0

        self.theme:str = "" #имя файла где лежат тесты # Заполняем на экране session
        self.topic: str = ""  # Название теста для элемента title # Заполняем на экране session

        self.ui:str = ""
        self.language:str = "ru"