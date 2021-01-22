#Repeated String

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
 l = len(s)
 a = 0
 if (n < l):
    sub = s[0:n]
    a = sub.count('a')
 else:
    times = n // l
    rest = n % l
    first = s.count('a')
    sub = s[0:rest]
    second = sub.count('a')
    a = times * first + second
 return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
