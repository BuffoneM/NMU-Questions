def fact(n):
    i = 1
    while(n > 1):
        i*=n
        n-=1
    return i

string = str(fact(60))[::-1]
count = 0
for char in string:
    if(char != '0'):
        break
    count+=1
print(count)