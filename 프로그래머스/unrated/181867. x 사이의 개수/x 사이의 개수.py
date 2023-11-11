def solution(myString):
    # 이거 길이 
    temp = myString.split("x")
    answer = []
    
    for i in temp :
        answer.append(len(i))
    
    return answer