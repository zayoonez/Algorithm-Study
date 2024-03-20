from collections import deque
def solution(arr):
    arr = deque(arr)
    answer = []
    answer.append(arr.popleft())
    while arr : 
        comp = arr.popleft()
        if comp != answer[-1] : 
            answer.append(comp)
            
    return answer