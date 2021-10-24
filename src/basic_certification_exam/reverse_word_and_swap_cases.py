#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#


def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    words = sentence.split()
    order_reversed = words[::-1]
    joined = ' '.join(order_reversed)
    swapped = joined.swapcase()
    return swapped


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
