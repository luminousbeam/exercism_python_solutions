import random
import string

class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def generate_alpha(self):
        alpha = string.ascii_letters
        rand_letter = random.choice(alpha.upper())
        return rand_letter        

    def generate_nums(self):
        rand_num = random.randint(100,999)
        return rand_num

    def generate_name(self):
        letter1 = self.generate_alpha()
        letter2 = self.generate_alpha()
        numbers = self.generate_nums()
        robo_name = letter1 + letter2 + str(numbers)
        return robo_name

    def reset(self):
        new_name = self.generate_name()
        if self.name == new_name:
            new_char = str(random.randint(0,9))
            self.name = new_name[:4]+ new_char
        else:
            self.name = new_name