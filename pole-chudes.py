import random
from words import words
import string

def get_word(words):
    random.shuffle(words)
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def pole_chudes():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed

    # getting user input
    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))
        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used this letter. Please try again!')
        else:
            print('Input error. Please try again!')

    print(f'You have guessed it. The hidden word is {word}')

pole_chudes()


