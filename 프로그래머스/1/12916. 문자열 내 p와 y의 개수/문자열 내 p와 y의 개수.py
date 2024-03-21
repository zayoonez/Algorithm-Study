from collections import deque
def solution(s):
    cnt = 0
    new = deque(s.lower())
    while new : 
        char = new.popleft()
        if(char == "p" ): 
            cnt += 1
        elif(char == "y") : 

            cnt -=1 
    if(cnt == 0) : 
        return True
    else : return False
    
