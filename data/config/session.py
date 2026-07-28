import random

class Session:
    def __init__(self,context):
        self.context = context
        self.user:str = ""
        self.questions = [] #список правильных ответов
        self.questions_noOK = [] #Список вопросов на которые ещё не отвечали
        self.question_count:int=0 #кол-во вопросов
        self.ask_count = 0 #Кол-во ответов
        self.ask_OK_count:int =0 #Кол-во правильных ответов
        self.ask_noOK_count:int =0 #Кол-во не правильных ответов
        self.ask_OK_index:int=0 #индекс правильного ответа
        self.ask_index:int=0 #индекс ответа
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

    #[x]: долучаем данные о вопросе и
    def get_answer(self,question_number):
        question = self.context.database.get_question(question_number, self.context.database.load_test(self.context.session.theme))  #получаем выбранный вопрос в виде словаря
        self.id = question["id"]
        self.question = question["question"]

        self.context.session.ask_count=self.context.session.ask_count+1    

        # Копируем ответы и перемешиваем
        self.answers = question["answers"].copy()
        random.shuffle(self.answers)


    def checking_answer(self, answer_index):
        """
        получаем индексный номер в списке ответов. 
        При этом в элемент списка состоит из 2 полей 
        - текст - текст ответа
        - correct - если правильно то true 
        """
        intAns = self.context.session.answers[answer_index]["text"]
        blAns = self.context.session.answers[answer_index]["correct"]
#цикл который будет проверяет ответы
        for x in range(len(self.context.session.answers)):
            if self.context.session.answers[x]["correct"]:
                self.context.session.ask_OK_index=x
                self.context.session.ask_index=answer_index
                if x == answer_index:
                  #индекс правильного ответа совпал с выбранным ответом
                    self.context.session.ask_OK_count=self.context.session.ask_OK_count+1
                    self.context.session.questions.append(self.context.session.id)
                    self.context.session.questions.sort()
                    self.context.session.questions_noOK.remove(self.context.session.id)
                    self.context.session.questions_noOK.sort()
                    return True
                #Если не совпал то записывам номер правильно ответа
                else:
                    self.context.session.ask_noOK_count=self.context.session.ask_noOK_count+1
                    return False

            


"""         
            if self.context.session.answers[answer_index]["correct"]:
            #print("Ответ правильный")
            #
            self.context.session.ask_OK_count=self.context.session.ask_OK_count+1
            self.context.session.questions.append(self.context.session.id)
            self.context.session.questions.sort()
            self.context.session.questions_noOK.remove(self.context.session.id)
            self.context.session.questions_noOK.sort()
            return True
        else:
            #print("Ответ не правильный")
            self.context.session.ask_noOK_count=self.context.session.ask_noOK_count+1             
            return False
 """        