"""https://programmers.co.kr/learn/courses/30/lessons/77484"""

#1st try
def solution(lottos, win_nums):
    num_zero = lottos.count(0)
    together = set(lottos + win_nums)
    together.discard(0)
    curr_match = 12 - len(together) - num_zero
    if curr_match == 6:
        return [1,1]
    elif num_zero == 0 and curr_match==0:
        return [6,6]
    elif curr_match == 0:
        return [1,6]
    else:
        return[7-curr_match - num_zero, 7-curr_match]
    return answer

#2nd try 
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)
    match = 0 
    for x in win_nums:
        if x in lottos:
            match += 1
    return [rank[match + cnt_0], rank[match]]
