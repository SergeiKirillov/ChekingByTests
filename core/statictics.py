class UserStatistics:
    def __init__(self, username):
        self.username = username
        self.learned_questions =set()
        self.total_correct=0
        self.total_wrong=0
    
    def is_learned(self, question_id):
        return question_id in self.learned_questions
    
    def mark_learned(self, question_id):
        self.learned_questions.add(question_id)
        

        