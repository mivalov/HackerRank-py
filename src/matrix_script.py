#!/bin/python3
""" Decode a matrix script

Matrix script N x M grid of strings. Consists of alphanumeric characters,
 spaces and symbols (!, @, #, $, %, &).

 [
    ['t', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['i', 'r', '!'],
 ]

To decode the script, Neo needs to read each column and select only the
alphanumeric characters and connect them. Neo reads the columns:
    - from top to bottom
    - from left to right
If there are symbols or spaces between two alphanumeric characters of the
decoded script, then Neo replaces them with a single space ' ' for better
readability.

Neo feels that there is no need to use 'if' conditions for decoding!

Alphanumeric characters consists of: [A-Z, a-z, and 0-9]

Input Format:
    The first line contains space-separated integers N (rows) and M (columns)
    respectively. The next N lines contain the row elements of the matrix
    script.

Constraints:
    0 < N, M < 100
    Note: A 0 score will be awarded for using 'if' conditions in the code

Output Format:
    Print the decoded matrix script.

Sample Input: (works with 3 chars per row, you might need to add spaces)
7 3
Tsi
h%x
i #
sM
$a
#t%
ir!

Sample Output:
    This is Matrix#  %!

Explanation:
    The decoded script is:
        - This is Matrix#  %!
    Neo replaces the symbols or spaces between two alphanumeric characters with
    a single space ' ' for better readability. So, the final decoded script is:
        - This is Matrix#  %!
"""

# import math
# import os
# import random
import re
# import sys

# specify N x M (rows x columns) of the matrix - default: '7 3'
first_multiple_input = input('Enter N x M:').rstrip().split()
# print('N x M:', first_multiple_input)

# n = 7 (rows)
n = int(first_multiple_input[0])
# print('n:', n)

# m = 3 (columns)
m = int(first_multiple_input[1])
# print('m:', m)

# define empty matrix as list
matrix = []
# print('Enter the matrix itself:')
for _ in range(n):
    # input the matrix itself (row by row)
    matrix_item = input()
    matrix.append(matrix_item)

print('matrix:', matrix)

# decoded script
decoded = [row[i] for i in range(m) for row in matrix]
decoded = ''.join(decoded)

# replace chars for readability
pattern = r'\b[^a-zA-Z0-9]+\b'
result = re.sub(pattern, r' ', decoded)
print(result)


""" Alternative solution with map() and 2x for-loops
n, m = map(int, input().split())
a, b = [], ''
for _ in range(n):
    a.append(input())
# print(a)
# print(type(a), type(b))

for z in zip(*a):
    print(b)
    b += ''.join(z)
    print(b)
# print(b)
print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', b))
"""