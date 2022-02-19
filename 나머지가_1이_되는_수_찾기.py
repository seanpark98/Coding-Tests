"""https://programmers.co.kr/learn/courses/30/lessons/87389"""

import math 

def solution(n):
    #Important rule: when checking for divisors, all you need to check to is the square root.
    for i in range(2, int(math.sqrt(n-1)) + 1):
        if (n-1) % i == 0:
            return i
    return n - 1