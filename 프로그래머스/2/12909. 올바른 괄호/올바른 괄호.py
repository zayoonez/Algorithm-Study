from collections import deque 
def solution(s):
    cnt = 0
    dq = deque(s)
    ## 회수가 되나 ..식이니까 한번에 cnt로 관리
    while(dq) :
        if dq.popleft() == '(' :
            cnt += 1
        else:
            cnt -= 1
        if cnt<0 :
            return False
    if(cnt ==0) : 
        return True
    else :
        return False