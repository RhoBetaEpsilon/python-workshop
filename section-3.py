'''Section 3: Exceptions in Python'''
'''
User input can be funky. Rather than have our program crash, we can handle the exceptions caused by bad input.
The code below creates a list of 100 random numbers, and the user can input the index in the list they want to see.
However, they can also input strings, floats, or numbers out of range. This causes the script to crash.
Add exception handling to re-prompt the user to enter a valid input. Make sure to let them know what they did wrong before!
'''
from random import randint

if __name__ == '__main__':
    readings = [randint(0, 100) for i in range(100)] # List of 100 random numbers
    user_input = input("Enter a number from 0 to 99: ")

    ### YOUR CODE HERE ###

    ''''''

    ### YOUR CODE ENDS ###

    print(readings[int(user_input)])