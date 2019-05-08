# https://www.hackerrank.com/challenges/crush/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign



#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    data = np.zeros(n)
    for (start, end, value) in queries:
        data[start - 1: end] += value
    return data.max()


def diffArrayManipulation(n, queries):
    data = [0] * (n + 1)
    for (start, end, value) in queries:
        data[start - 1] += value
        data[end] -= value
    start = data[0]
    _max = data[0]
    for each in data[1:]:
        _new = start + each
        if _new > _max:
            _max = _new
    return _max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
