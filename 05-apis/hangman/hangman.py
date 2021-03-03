import requests

"""
Retrieves a random word from an API and displays with characters hidden for the hangman game.
OPTIONAL EXERCISES:
1. continue and complete the hangman game so that the user will select letters.
2. build in Tkinter and draw the hangman!
"""

class Hangman:
    def __init__(self):
        self.word = ''
        self.secret = ''

    def get_random_word(self):
        response = requests.get('https://random-word-api.herokuapp.com/word?number=1')
        if response.status_code != 200:
            print('Error', response.status_code)
        else:
            word_list = response.json()
            self.word = word_list[0]
            self.make_secret()

    def make_secret(self):
        self.secret = self.word[0] + ('_'*(len(self.word)-2)) + self.word[-1]


if __name__ == '__main__':
    hangman = Hangman()
    hangman.get_random_word()

    print(hangman.word)
    print(hangman.secret)

