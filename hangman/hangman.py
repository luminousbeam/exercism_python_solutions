# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = "_" * len(self.word)

    def guess(self, char):
        result = self.word.find(char)
        self.remaining_guesses -= 1
        if result == -1:
            self.result_check()
            return 
        temp = self.masked_word[0:result] + char + self.masked_word[result + 1:]
        print(f'result {result}')
        print(f'result + 1 {self.masked_word[result + 1:]}')
        self.masked_word = temp
        self.result_check()

    def result_check(self):
        print(self.remaining_guesses)
        if self.word == self.masked_word:
            self.status = STATUS_WIN
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

game = Hangman('for')
game.guess('f')
game.guess('o')
game.guess('r')

print(game.get_masked_word())
print(game.get_status())
