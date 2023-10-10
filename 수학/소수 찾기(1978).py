n = int(input())
num = list(map(int,input().split()))
cnt = 0
flag = 0
for i in num:
    if i != 1:
        for j in range(2,i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            cnt += 1
        else:
            flag = 0
print(cnt)