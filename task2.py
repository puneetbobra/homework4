# Create a function that randomly generates and returns a tuple of two positive one-digit integers. 
# Then prompt the user for the multiplication of the two numbers
# Compare the user's answer with the correct result. If the answer is correct, display a message “done”. Otherwise keep asking the user

import random

# define function which generates 2 random numebrs and returns 2 positive 1 digit number
def random_number():
    '''Function to generate 2 positive random 1 digit integers'''
    number_1 = random.randrange(1,10)
    number_2 = random.randrange(1,10)
    return (number_1, number_2) # pack the random integer in to a tuple

number = random_number() #unpack the tuples in to a variable

# compute the multiplication of the tuples
result = number[0] * number[1]

# Ask user input for the result of multiplication and continue asking until the user is correct
while True:
    print('How much is', number[0], 'times', number[1], '?')
    user_answer = int(input())
    if user_answer == result: 
        print('Done')
        break
    else: 
        print(number[0], 'times', number[1], 'is not', user_answer)
        continue

# End



