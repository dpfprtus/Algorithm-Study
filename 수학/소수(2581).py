m = int(input())
n = int(input())
sosu = []
flag = 0
for i in range(m,n+1):
    if i != 1:
        for j in range(2,i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            sosu.append(i)
        else:
            flag = 0
if sosu:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)

        
