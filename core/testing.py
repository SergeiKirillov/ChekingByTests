import random

class Testing():
    def __init__(self, number):
       self.exclude=number
        
        
    def rand_ans(self):
        available = [
            x for x in range(1, 201)
            if x not in self.exclude
        ]

        if not available:
            raise ValueError("Свободных чисел не осталось")

        number = random.choice(available)
        self.exclude.append(number)

        return number


    

    