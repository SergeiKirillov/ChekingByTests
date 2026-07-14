
class Session:
    def __init__(self):
        self.user:str = ""
        self.topic:str = "" #Название теста для элемента title
        self.questions = []
        self.questions_index:int = 0
        self.correct:int = 0
        self.theme:str = "" #имя файла где лежат тесты
        self.ui:str = ""
        self.language:str = "ru"