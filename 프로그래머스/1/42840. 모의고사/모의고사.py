def solution(answers) :
    student1 = [1, 2, 3, 4, 5] 
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    r1=0
    r2=0
    r3=0
    score = [0, 0, 0]
    result = []
    #answers 길이가 13일 때 
    for i in range(len(answers)):
        if(student1[i % 5] == answers[i]) : 
            score[0] += 1
        if(student2[i % 8] == answers[i]) : 
            score[1] += 1
        if(student3[i % 10] == answers[i]) : 
            score[2] += 1
    for idx, s in enumerate(score) : 
        if(max(score) == s):
            result.append(idx+1)
    return result