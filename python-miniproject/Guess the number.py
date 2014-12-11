"""
需求： 猜数字  https://class.coursera.org/interactivepython-005/human_grading/view/courses/972530/assessments/29/results/mine
#One of the simplest two-player games is “Guess the number”. The first player thinks of a secret number in some known range while the second player attempts to guess the number. After each guess, the first player answers either “Higher”, “Lower” or “Correct!” depending on whether the secret number is higher, lower or equal to the guess. In this project, you will build a simple interactive program in Python where the computer will take the role of the first player while you play as the second player.

#You will interact with your program using an input field and several buttons. For this project, we will ignore the canvas and print the computer's responses in the console. Building an initial version of your project that prints information in the console is a development strategy that you should use in later projects as well. Focusing on getting the logic of the program correct before trying to make it display the information in some “nice” way on the canvas usually saves lots of time since debugging logic errors in graphical output can be tricky.
"""


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math
secret_number =0
flag =100
n =0 
# helper function to start and restart the game
def new_game():
    print "\nnew start " 
    global secret_number,n
    # initialize global variables used in your code here
    secret_number = random.randrange(0, flag)
    n = int(math.ceil(math.log(flag+1, 2))) 
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "\nguess:Range: 0 - 100"
    global flag  
    flag = 100
    new_game()   

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "\nguess:Range: 0 - 1000"
    global flag  
    flag = 1000 
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global n
    n-=1
    number = int(guess)
    print "\nyou input number is ",number
    if  number > secret_number: 
        print "Lower"
    elif number <  secret_number:
        print "Higher"
    else:
        print "Correct"
        print "game over~~ hahaha~"
        new_game()
        return 
    if n<1:	
        print "game over~~ hahaha~"
        new_game()
        return   
    print "left guess time(s):",n
        
    
# create frame
frame = simplegui.create_frame('input_guess', 100, 200)
frame.add_button("guess:Range: 0 - 100",range100 )
frame.add_button("guess:Range: 0 - 1000",range1000 )
frame.add_input('input_guess', input_guess, 100)
# register event handlers for control elements and start frame


# call new_game 
new_game()
# always remember to check your completed program against the grading rubric
