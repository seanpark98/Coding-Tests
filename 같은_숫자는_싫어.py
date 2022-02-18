"""https://programmers.co.kr/learn/courses/30/lessons/12906"""

#1st try 
def solution(arr):
    ans = []
    for i in arr:
        if len(ans) == 0:
            ans.append(i)
        else: 
            if ans[-1] == i:
                continue
            else:
                ans.append(i)
    return ans

#2nd try
def solution(arr):
    ans = []
    for i in arr:
        #slice to not make another if statement
        if ans[-1:] == [i]:
            continue
        ans.append(i)
    return ans
