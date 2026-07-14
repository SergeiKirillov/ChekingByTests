import random

class TestSession_0:
    def __init__ (self, questions):
        
        self.correct_count=0
        self.wrong_count=0

        self.active_questions = questions.copy()

        random.shuffle(self.active_questions)
    
    def has_questions(self):
        return len(self.active_questions)>0
    
    def get_next_question(self):
        if not self.active_questions:
            return None
        
        q= self.active_questions.pop(0)
        q.shuffle_answers()
        return q
    
    def process_answer(self, question, answer_index):
        selected = question.answers[answer_index]
        
        if selected.correct:
            self.correct_count += 1
            return True
        self.wrong_count +=1
            #ошибочный вопрос возвращаем в конец очереди
        self.active_questions.append(question)

        return False 
    
class TestSessions:
    def __init__(self,
                 questions,
                 statistics, 
                 settings,
                 mode):
        
        self.mode=mode
        self.statictics = self.statistics
        self.correct_answers=0
        self.wrong_answers=0

        available_questions = []
        for q in questions:
            if not statistics.is_learned(q.id):
                available_questions.append(q)

            random.shuffle(available_questions)

            self.questions = available_questions[
                :settings.questions_per_session
                ]
            self.current_index = 0
    #Получение следующего вопроса
    def get_next_question(self):
        if self.current_index >= len(self.questions):
            return None
        question = self.questions[self.current_index]
        self.current_index += 1
        question.shuffle_answers()
        return question
    #Проверка ответа
    def process_answer(
        self,
        question,
        answer_index):
        
        selected = question.answers[answer_index]
        if selected.correct:
            self.correct_answers += 1
            self.statistics.mark_learned(
                question.id
            )
            self.statistics.total_correct += 1
            return True
        self.wrong_answers += 1
        self.statistics.total_wrong += 1
        return False


