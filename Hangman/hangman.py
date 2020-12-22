import json
import random
import string

data = json.load(open("D:/Data Science/Python/Programs/mini-projects/Hangman/words.json"))


def get_valid_word():
    word = random.choice(data)
    while '-' in word or ' ' in word:
        words = random.choice(data)
    return word.upper()


def hangman():
    word = get_valid_word()
    word_letters = set(word)    # letters in the word
    alphabet = list(string.ascii_uppercase)
    used_letters = []   # letters which user has guessed
    lives = 6   # no of attempts 

    while len(word_letters) > 0 and lives > 0:
        # what is current word : H-L-O
        current_word = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(current_word), "\n")

        print("You have",lives,"lives left!!")

        # letters guessed by user
        print("These are the Letters you have used:", " ".join(used_letters))

        # Letter input from User
        user_letter = input("Guess a Letter: ").upper()
        if user_letter not in used_letters and user_letter in alphabet:
            used_letters.append(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print("You have already used that letter. Try again!")
        else:
            print("Invalid Character.")


    if lives == 0:
        print('''You Die!! Sorry.
The word was''', word)
    else: print("Yay! You guess the word", word, "correctly!!")



hangman()
