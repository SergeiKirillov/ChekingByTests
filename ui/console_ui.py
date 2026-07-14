class ConsoleUI_0:

    def ask_question(self, question):

        print()
        print(question.question)

        for i, answer in enumerate(question.answers, start=1):
            print(f"{i}. {answer.text}")

        return int(input("Ваш ответ: ")) - 1
    
class ConsoleUI:
    def show_question(self, question):
        print()
        print(question.question)
        for i, answer in enumerate(
                question.answers,
                start=1):
            print(
                f"{i}. {answer.text}"
            )
        return int(
            input("Ответ: ")
        ) - 1
    def show_result(result):
        print()
        print("Тест завершён")

        print(
            f"Правильных: "
            f"{result.correct_answers}"
        )
        print(
            f"Ошибок: "
            f"{result.wrong_answers}"
        )
    