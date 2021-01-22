#Jumping on the Clouds

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
 jump = 0
 total = len(c)-2
 i = 0
 while (i < total+1):
  if c[i] == 0 and i == total:
    if c[i+1] == 0:
     jump+=1
  if c[i] == 0 and i < total:   
   next = i+2
   print (i)
   if c[next] == 1:
    jump+=1
   if c[next] == 0:
    i+=1
    jump+=1
#  if c[i+1] == 0 and i+1 == total: 
#    jump+=1 
  i+=1
 return jump
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
