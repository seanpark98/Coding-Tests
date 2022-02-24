"""https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3"""

#1st try, didn't work
def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    hand_dict = {'left': 'L', 'right': 'R'}
    #why did I use a while loop when I could use a for loop?
    while numbers != []:
        curr_num = numbers[0]
        if curr_num == 0:
            curr_num = 11
        if curr_num == 1 or curr_num == 4 or curr_num == 7:
            left = curr_num
            answer += 'L'
            #with a for loop you wouldn't need to slice. Also it would have been better to put the slicing before the if statements began
            numbers = numbers[1:]
        elif curr_num == 3 or curr_num == 6 or curr_num == 9:
            right = curr_num
            answer += 'R'
            numbers = numbers[1:]
        else:
            if (left + 2) == right or abs(curr_num - left) == abs(curr_num - right):
                answer += hand_dict[hand]
                if hand_dict[hand] == 'L':
                    left = curr_num
                else: 
                    right = curr_num
                numbers = numbers[1:]
            else:
                if abs(curr_num - left) > abs(curr_num - right):
                    right = curr_num
                    answer += 'R'
                    numbers = numbers[1:]
                else:
                    left = curr_num
                    answer += 'L'
                    numbers = numbers[1:]
    return answer

import math

#2nd try
def solution(numbers, hand):
    answer = ''
    left = [0,3]
    right = [2,3]
    dic = {1: [0,0], 2: [1,0], 3:[2,0], 4:[0,1], 5:[1,1], 6:[2,1], 7: [0,2], 8:[1,2], 9:[2,2], 0:[1,3]}
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = dic[i]
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = dic[i]
        else:
            if distance(dic[i], left) == distance(dic[i], right):
                if hand == 'left':
                    answer += 'L'
                    left = dic[i]
                else:
                    answer += 'R'
                    right = dic[i]
            elif distance(dic[i], left) > distance(dic[i], right):
                answer += 'R'
                right = dic[i]
            else:
                answer += 'L'
                left = dic[i]       
    return answer

#key is using a different distance function then you would normally use for an x,y plane
def distance(cord1, cord2):
    return abs(cord2[0] - cord1[0]) + abs(cord2[1] - cord1[1])