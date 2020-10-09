#Write a Boolean function named is_prime which takes an integer as an argument
#and returns true if the argument is a prime number, or false otherwise. 

def is_prime(number):
    """A prime number is a number that is only evenly divisble by itself and 1.
    For example, the number 5 is prime because it can only be evenlly divided by 1
    and 5. The number 6, however, is not prime because it can be divided evenly
    by 2 and 3."""
    #number will be a prime number if the remainder is 0 only 2 times when then number is divided by 1 until itself
    #initialize variable to count the remainder being 0
    count = 0
    for i in range (1,number+1):
        is_prime = number % i
        if is_prime == 0:
            count += 1        
        else: count = count
        i += 1

    if count == 2:
        return True
    elif count > 2:
        return False

# Write a program that generates six random number between 1 and 100 (inclusive) and print out the result
import random

for i in range (1,7):
    #generate random number from 1 until 100 (both inclusive)
    number = random.randrange(1,101)
    #call is_prime function for the random number generated
    is_prime(number)
    #check if is_prime is true or false and print prime number status accordingly
    if is_prime(number) == True:
        print('The random number', number ,'is a prime number')
    elif is_prime(number) == False:
        print('The random number', number, 'is not a prime number')

#End