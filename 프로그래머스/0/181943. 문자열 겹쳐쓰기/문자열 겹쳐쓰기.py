def solution(my_string, overwrite_string, s):
    new = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return new