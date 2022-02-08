"https://programmers.co.kr/learn/courses/30/lessons/68935"

#1st try
def solution(n):
    ternary = ''
    answer = 0
    while n:
        n,r = divmod(n, 3)
        ternary += str(r)
    mult = 1
    ternary = int(ternary)
    while ternary:
        ternary, curr = divmod(ternary, 10)
        answer += curr * mult
        mult *= 3
    return answer

#2nd try
def solution(n):
    tmp = ''
    while n:
        n, rem = divmod(n, 3)
        tmp += str(rem)
    #int takes base as a parameter
    return int(tmp, 3)