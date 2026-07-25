import random

class Session:
    def __init__(self,context):
        self.context = context
        self.user:str = ""
        self.questions = [] #список правильных ответов
        self.questions_noOK = [] #Список вопросов на которые ещё не отвечали
        self.ask_count = 0 #Кол-во вопросов
        self.questions_index:int = 0
        self.correct:int = 0

        self.theme:str = "" #имя файла где лежат тесты # Заполняем на экране session
        self.topic: str = ""  # Название теста для элемента title # Заполняем на экране session

        self.id:int=0 #Номер вопроса
        self.question:str="" #вопрос
        self.answers:list=[] #список ответов

        self.ui:str = ""
        self.language:str = "ru"


    #TODO: Переносим логику работы по выбору вопросов в класс session

    #[x]: генерируем случайное число
    def rand_ans(self):
        if not self.questions_noOK:
            available = [
                x for x in range(1, 201)
                if x not in self.questions
            ]
            if not available:
                raise ValueError("Свободных чисел не осталось")
            else:
                self.questions_noOK = available

        #number = random.choice(available)
        number = random.choice(self.questions_noOK)
#        self.exclude.append(number)
        return number

    #[ ]: долучаем данные о вопросе и
    def get_answer(self,ask_number):
        question = self.context.database.get_question(ask_number, self.context.database.load_test(self.context.session.theme))  #получаем выбранный вопрос в виде словаря
        self.id = question["id"]
        self.question = question["question"]

        # Копируем ответы и перемешиваем
        self.answers = question["answers"].copy()
        random.shuffle(self.answers)

