# wordle word game
import random
from english_words import get_english_words_set

# functions
def dictionary_by_size(dictionary, n_letters):
    return [word for word in dictionary if len(word) == n_letters]

# Main code

# Create a dictionary of all english words
dictionary = tuple(get_english_words_set(['web2'], lower=True))

# Cut down dictionary to N number of letter words
n_letters = int(input("Hello, welcome to WORDLE\n Please input the number of letters you would like: "))
random_word = random.choice(dictionary_by_size(dictionary,n_letters))

wordle = random_word
wordle_feedback = [0] * len(wordle)
#print(wordle)

# Input guesses for word
cond_wordle = False
cond_fail = False
n_guess = 0

while cond_wordle == False and cond_fail == False:

    n_guess = n_guess +1
    guess = input(f"Please make your #{n_guess} {n_letters}-letter guess: ")
    # make it so guesses with wrong number letters are barred but allow next guess
    while len(guess) != n_letters or guess.isalpha() == False :
        guess = input(f"Your guess was not valid! Please guess again using {n_letters} alphabet letters. Next guess: ")
    if guess == wordle:
        cond_wordle = True
        print("Congrats!!! You achieved Wordle success")
        print (f"The word was {wordle.upper()}!")
        break
    else:
        for pos, character in enumerate(guess):
            if wordle[pos] == character:
                wordle_feedback[pos] = character.upper()
            elif wordle.find(character) != -1:
                wordle_feedback[pos] = character.lower()
            else:
                wordle_feedback[pos] = "_"
        print(wordle_feedback)
    # limit number of guesses
    if n_guess >= 6:
        cond_fail = True
        print(f"You ran out of guesses :( The wordle was {wordle}. Better luck next time!")



# if uppercase letter already present repeat of this letter will still show lowercase - fix?


