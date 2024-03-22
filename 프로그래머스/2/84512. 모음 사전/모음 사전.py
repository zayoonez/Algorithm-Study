# AEIOU
from itertools import product
answers = []
def solution(word):
    words = "AEIOU"
    for i in range(1, 6) : 
        for j in product(words, repeat = i) : 
            answers.append(''.join(j))
    return sorted(answers).index(word)+1
        