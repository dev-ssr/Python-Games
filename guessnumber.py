# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

global secret_number, x
hr_range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    # remove this when you add your code
    global secret_number, x
    secret_number = random.randrange(0,hr_range)
    print("\nRange : 0 - "+ str(hr_range))
    x = int(math.ceil(math.log(hr_range+1,2)))
    print ("You have "+str(x)+" guesses")


# define event handlers for control panel
def range100():
    global hr_range
    hr_range = 100
    new_game()
    #print(secret_number)

def range1000():
    global hr_range
    hr_range = 1000
    new_game()
    #print(secret_number)

def input_guess(guess):
    # main game logic goes here
    global x
    x -= 1
    print("\nYou guessed : "+guess)
    guess = int(guess)
    print ("You have "+str(x)+" guesses")
    if x >= 0 :
        if guess > secret_number:
            print("Lower")
        elif guess < secret_number:
            print("Higher")
        else:
            print("Correct!")
            new_game()
    else:
        print("Game Over!")
        new_game()


# create frame
frame = simplegui.create_frame("Guess the number!",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range [0 - 100) ",range100)
frame.add_button("Range [0 - 1000) ",range1000)
user_guess = frame.add_input("Enter your guess",input_guess,100)

# call new_game
frame.start()
#print("Range 0 -100 selected")
new_game()


# always remember to check your completed program against the grading rubric
