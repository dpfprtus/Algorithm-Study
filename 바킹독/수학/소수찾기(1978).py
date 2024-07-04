n = int(input())

nums = list(map(int,input().split()))
result = 0
flag = 0
for num in nums:
    for j in range(2,num):
        if num % j == 0:
            flag = 1
            break
    if flag == 0 and num != 1:
        result += 1
    flag = 0
print(result)