#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    total = 0
    curr = p
    count = 0
    if s > 0:
        while total <= s:
            total += curr
            if (curr-d) > m:
                curr -= d
            count += 1
            print(total, " ", count)
    return count-1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print(answer)

    # fptr.write(str(answer) + '\n')

    # fptr.close()
