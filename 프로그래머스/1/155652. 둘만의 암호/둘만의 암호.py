def solution(s, skip, index):
    alph = "abcdefghijklmnopqrstuvwxyz"
    answer = ''

    for i in skip :
        alph = alph.replace(i, '')
    
    for char in s :
        answer += alph[(alph.find(char) + index) % len(alph)]
    return answer
    
