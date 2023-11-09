def solution(array, commands):
    answer = []
    for i, j, k in commands : 
        temp = sorted(array[i-1 : j])
        answer.append(temp[k-1])
    return(answer)

# def solution(array, commands):
# #     commands는 이차원 배열
#     temp = []
#     answer = []
#     for i in range(len(commands)) : 
#         num = commands[i][2]-1
#         temp = array[commands[i][0]-1 : commands[i][1]]
#         temp.sort()
#         answer.append(temp[num])
#     return(answer)