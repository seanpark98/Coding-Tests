"""https://programmers.co.kr/learn/courses/30/lessons/12982"""

#1st try
def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    else:
        d.sort()
        cnt = 0
        for i in d:
            budget -= id
            if budget < 0:
                break
            cnt +=1
        return cnt