def solution(t, p):
    count = 0
    for i in range(len(t)-len(p) +1) :
        # print(i)
        part_t = t[i:(i+len(p))]
        if (int(part_t) - int(p) <= 0) :
            count += 1
    return count
    
        
    # answer = 0
    # return answer