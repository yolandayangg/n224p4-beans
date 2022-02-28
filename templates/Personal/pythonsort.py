from random import randrange
import random

 # Pick random number between 1 and 100.

x = random.randint(1, 100)
print (x)


if (x % 2) == 0 :
    print("Even")
else:
    print("Odd")

if (x == 1):
    print("Prime Number")
else:
    for i in range (2,x):
        x_is_prime = 'true'
        if (x%i == 0):
            print("Not a Prime Number")
            x_is_prime = 'false'
            break
    if (x_is_prime == 'true'):
        print("Prime Number")




