def solution(k, m, score):
    answer = 0
    box = len(score) % m
    score.sort(reverse = True)
    list = [score[i * m : (i * m) + m] for i in range(0, len(score)//m)]
    
    for i in list : 
        answer += min(i) * m
    return answer