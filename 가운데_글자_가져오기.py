"""https://programmers.co.kr/learn/courses/30/lessons/12903"""

def solution(s):
    #If the number is odd then the diff between the two is 1, but if its even then the diff become two
    return s[(len(s)-1)//2:len(s)//2+1]