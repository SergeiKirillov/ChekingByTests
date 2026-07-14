import  random

class Question_v2:
    def __init__(self, question_data):
        self.id = question_data["id"]
        self.question = question_data["question"]
        self.comment = question_data.get("comment","")

        #Копируем ответы и перемешиваем
        self.answers=question_data["answers"].copy()
        random.shuffle(self.answers)

    def show(self):
        """Отображение вопроса и вариантов ответа"""
        print(f"\nВопрос №{self.id}")
        print(self.question)
        print()

        for i, answer in enumerate(self.answers, start=1):
            print(f"{i}. {answer['text']}")

    def check_answer(self, user_choice):
        """
        Проверка ответа пользователя.
        user_choice - номер выбранного варианта (1..N)
        """
        if not (1 <= user_choice <= len(self.answers)):
            return False

        return self.answers[user_choice - 1]["correct"]

    def get_correct_answer(self):
        """Возвращает текст правильного ответа"""
        for answer in self.answers:
            if answer["correct"]:
                return answer["text"]




       
