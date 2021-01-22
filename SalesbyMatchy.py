#Sales by Match
#Shelly Leal
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
 ob = ar[0]
 j = set()
 pairs = 0
 for sock in ar:
    if sock not in j:
      j.add(sock)   
    else:
      pairs += 1
      j.remove(sock)
 return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
