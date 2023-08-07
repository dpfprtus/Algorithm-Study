
from re import L


n,m,k = map(int,input().split())
number = list(map(int,input().split()))
number.sort(reverse=True)
number = number[:2]
result = 0
x = 0
print(number)
while(m > x):
    print(x)
    for j in range(k):
        if (x >= m):
            break
        result += number[0]
        x += 1
    if(x>=m):
        break
    result += number[1]
    x += 1
    
print(result) 