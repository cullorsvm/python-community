##FOR loops (review my PPT) #3
##How FOR uses the RANGE attribute with integers.
##Use Python Standard Library - have them look up the RANDOM library and read how to use, must IMPORT into program #4
##Importance of formatting the code - EXAMPLE: what happens if print (y,z) was not indented? demostrate this #5


##Python program 1
##SIMPLE INTRO to roll dice

##1 import a Python library
import random

##2 get string input, convert input into integer type
roll_time = input('Enter how many times to roll dice > ')
x_times   = int(roll_time)

##3 print output header
print ("Die1 Die2")
print ("------------")

##4 FOR loop to roll dice set by user input and print each rolls
for x in range(x_times):
    print ("x = " + str(x))
    ##5 get random integer numbers between 1 and 6
    y = random.randint(1,6)
    z = random.randint(1,6)
    ##6 print out the random numbers
    print (y , z)

##7 print out
print ("Dice rolled " + roll_time + " times.")
print ("Script complete.") 
