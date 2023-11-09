str = input()
newStr = ""

for i in str :
    if(i.islower()) :
        newStr += i.upper()
    else :
        newStr += i.lower()
    
print(newStr)