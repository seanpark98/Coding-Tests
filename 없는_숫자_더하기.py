"https://programmers.co.kr/learn/courses/30/lessons/86051"

#1st try
def solution(numbers):
    answer = 0
    for i in range(0, 10):
        if i not in numbers:
            answer += i 
    return answer

#better answer
def solution(numbers):
    return 45 - sum(numbers)