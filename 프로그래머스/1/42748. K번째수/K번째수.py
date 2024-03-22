# i 번째부터 j 까지 
def solution(array, commands):
    answer = []
    
    # print(array[commands[0]-1:commands[1]-1])
    for i in range(len(commands)) : 
        start = commands[i][0]-1
        end = commands[i][1]
        idx = commands[i][2]-1
        new = sorted(array[start:end])
        answer.append(new[idx])
        
    return answer