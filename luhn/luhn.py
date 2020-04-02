import re

class Luhn:
    def __init__(self, card_num):
        self.card_num=card_num.replace(' ', '')
        
    def valid(self):
        card_num=list(self.card_num)
        for i in range(len(card_num)):
            if card_num[i].isdigit() == False:
                return False
            card_num[i]=int(card_num[i])

        if len(card_num) < 2:
            return False

        for i in range(len(card_num)-2,-1,-2):
                if card_num[i]*2<=9:
                    card_num[i]*=2
                else:
                    card_num[i]=card_num[i]*2-9
        
        return True if sum(card_num) % 10 is 0 else False
