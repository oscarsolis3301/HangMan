from random import randint
import tkinter
from scenarios import scenarios
from art import *

tprint(text="Hangman")

# window = tkinter.Tk(className = "ultimate hangman")

# window.geometry("700x500")

# display_art = tkinter.Label(window, text=art, width=300, height=500)
# display_art.pack()

# exit = tkinter.Button(window, text="Exit", command=window.destroy)
# continue_button = tkinter.Button(window, text="Continue", command=print(scenarios[0]))

# window.columnconfigure(0, weight=0)
# window.rowconfigure(0, weight=0)
# window.columnconfigure(1, weight=1)
# window.rowconfigure(1, weight=1)
#exit.grid(row=0, column=1)
#continue_button.grid(row=1, column=1)

# Tkinter main loop
#window.mainloop()
# End of Tkinter

words=['laptop', 'bee', 'phone']

running = True

random_word=words[randint(0,2)]

size_of_word=len(random_word)

underscores=''

count=0


print('Welcome to hangman! <3 by beb & beb')
print('  _____')
print('  |   |')
print('      |')
print('      |')
print('      |')
print(' _____|___')

#scenarios bc beb is smelly <3


guessed_correctly=0
guessed_letters = size_of_word * ['_']
print(' '.join(guessed_letters))
scenario_count = 0
GameIsDone = False
def PlayAgain():
    play_again = input("Do you want to play again?")
    return play_again.lower

while True:

    guessed_word=''
    correct_answer = False
    found_before = False
    correct_letter_count = 0
    guesses=['']
    user_guess=input('Please enter a letter: ')
    if user_guess != guesses:
        print('no')
    else:
        guesses.append(user_guess)
    for x in range(size_of_word):
        if user_guess == random_word[x]:
            guessed_letters[x] = user_guess
            correct_letter_count+=1
            correct_answer = True
    
    if(correct_answer == True):
        print('You found ' + str(correct_letter_count) + " correct letters in the word!")
        print(' '.join(guessed_letters))

    else:
        if(scenario_count==6):
            GameIsDone = True
        else:
            print(scenarios[scenario_count])
            scenario_count+=1
            print(' '.join(guessed_letters))
            continue

    for x in guessed_letters:
        guessed_word+=x

    if(guessed_word == random_word):
        print("YOU HAVE FINISHED THE GAME GG.")
        GameIsDone = True
    else:
        continue 
    if GameIsDone == True:
        if PlayAgain() == "y" or "yes":
            guessed_correctly=0
            random_word=words[randint(0,2)]
            size_of_word = len(random_word)
            guessed_letters = size_of_word * ['_']
            guesses=[]
            scenario_count = 0
            print('\n')
            print('  _____')
            print('  |   |')
            print('      |')
            print('      |')
            print('      |')
            print(' _____|___')
            print(' '.join(guessed_letters))
            GameIsDone = False
        else:
            break
