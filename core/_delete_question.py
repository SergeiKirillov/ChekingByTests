class Question:
    def __init__(self, q_id, topic, question, answers, comment=""):
        self.id=q_id
        self.topic=topic
        self.question=question
        self.answers=answers
        self.comment=comment
    def shuffle_answers(self):
        import random
        random.shuffle(self.answers)

