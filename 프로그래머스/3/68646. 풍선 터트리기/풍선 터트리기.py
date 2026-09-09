from heapq import heappush, heappop, heapify

def solution(a):
    answer = 0
    num = len(a) - 1
    min_idx_left = 0
    min_idx_right = num
    min_list_left = []
    min_list_right = []
    
    
    for i in range(len(a)):
        if a[i] < a[min_idx_left]:
            min_idx_left = i
        if a[num - i] < a[min_idx_right]:
            min_idx_right = num - i
        min_list_left.append(a[min_idx_left])
        min_list_right.append(a[min_idx_right])
        
        if i == len(a) - 1:
            min_idx = min_idx_left
    
    min_list_right = list(reversed(min_list_right))
    
    for i in range(len(a)):
        
        if i < min_idx and min_list_left[i] == a[i]:
            answer += 1
        elif i > min_idx and min_list_right[i] == a[i]:
            answer += 1
        elif i == min_idx:
            answer += 1
    return answer