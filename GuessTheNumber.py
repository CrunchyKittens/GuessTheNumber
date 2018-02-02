'''
Created on Feb 3, 2018

@author: Mike Noble

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
'''
import random

print "Welcome I'm thinking of a number between 1 & 9"
print "Can you guess what it is?"
print ""
# get random number between 1 and 1000
num = random.randint(1,1000)

#add counter to while loop to count the number of guesses it takes to get the correct answer
count = 0
#repeat loop until user gets the correct answer
breakLoop = False
while (breakLoop == False):
    
    #ask user to guess the number
    guess = int(raw_input("Enter a number between 1 & 1000"))
    print ""
   
    #   compare user values with the random number. inform user if the guess is to high, low or correct
    if (guess > num):
        print "To High!"
        print "Guess again."
        count +=1
    elif (guess < num):
        print "To Low!"
        print "Guess Again!"
        count +=1
    else:
        print str(num)+" Is Correct. Well done!" 
        print "You found the answer in "+str(count)+" guesses"
        breakLoop = True

