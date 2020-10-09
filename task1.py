#Write a Boolean function named is_prime which takes an integer as an argument
#and returns true if the argument is a prime number, or false otherwise. 

#1. create a boolean function named is_prime
#2. 

def is_prime(number):
    """A prime number is a number that is only evenly divisble by itself and 1.
    For example, the number 5 is prime because it can only be evenlly divided by 1
    and 5. The number 6, however, is not prime because it can be divided evenly
    by 2 and 3."""
    count = 0
    for i in range (number):
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



