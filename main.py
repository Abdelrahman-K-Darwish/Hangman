import random

'''
    The hangman shape divided into different lines
'''
Hangman_shape = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

'''
    a function to select a word randomly from a hard-coded set of words 
'''
def get_a_random_word():
    words = [
        'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
        'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
    ]
    return random.choice(words)

class Hangman:
    """
    Failed_attempts -> a variable to count the number of missed characters the user inserted
    word_to_guess -> the word that the user should guess a character by a character
    game_progress -> a list of underscores and each time the user guesses a character correctly it gets placed instead
    of the underscore in its place
    """
    def __init__(self):
        self.failed_attempts=0
        self.word_to_guess = get_a_random_word()
        self.game_progress=list('_' * self.word_to_guess.__len__())

    """
    a static method to make sure that the given variable is holding a character ( 1 and only )
    """
    @staticmethod
    def validate_input(letter):
        if letter.isdigit() or (letter.isalpha() and letter.__len__() > 1):
            return False
        else:
            return True
    """
    a function to read the input from the user and validates the input 
    """
    def get_input(self):
        letter = input("please enter a char : ")
        if Hangman.validate_input(letter):
            return letter
        else:
            print("Please check the input you inserted as it's not valid")
            return None
    """
    a method to get the indices of the letter given in the word_to_guess
    """
    def find_indices(self, letter):
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]
    """
    a method to swap the underscore with the character guessed correctly
    """
    def update_game_progress(self,indices):
        for index in indices:
            self.game_progress[index]=self.word_to_guess[index]

    """
    a method to run the automation of the game
    """
    def play(self):
        print('----------------------------------  let us start the show  ----------------------------------' )
        while self.failed_attempts < Hangman_shape.__len__() :
            print(self.game_progress)
            letter = self.get_input()
            if letter is None :
                print('Oops! , seems like your insertion was not a letter please try again')
            else:
                if letter in self.game_progress:
                    print("You have already guess that letter")
                else:
                    indices = self.find_indices(letter)
                    if indices.__len__() > 0 :
                        print("Marvelous! You guess a character")
                        self.update_game_progress(indices)
                        if not self.game_progress.count('_'):
                            print("Seems like you made it alive, Congrats you won :)")
                            return
                    else :
                        print("You missed your chance mate")
                        self.failed_attempts += 1

        print('Drop dead - you lost')
        for i in Hangman_shape :
            print(i)





if __name__ == '__main__':
    Game=Hangman()
    Game.play()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
