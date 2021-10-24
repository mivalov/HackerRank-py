#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizz_buzz(n):
    # Write your code here
    for i in range(n+1):
        if i == 0:
            continue
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 3 != 0 and i % 5 == 0:
            print('Buzz')
        else:
            print(i)


if __name__ == '__main__':
    a = 15
    fizz_buzz(a)
