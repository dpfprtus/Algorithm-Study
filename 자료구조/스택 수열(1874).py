n = int(input())
num = []
stack = []
for i in range(n):
    num.append(int(input()))

result = [0]
result1 = []
cnt = 0
for i in range(n):
    if num[i] > result[-1]:
        while num[i] > cnt:
            cnt+=1
            result.append(cnt)
            result1.append("+")
    if num[i] == result[-1]:
        stack.append(result.pop())
        result1.append("-")
        continue
    elif num[i] < result[-1]:
        while num[i] < result[-1]:
            result.pop()
            result1.append("-")

if stack != num:
    print("NO")
else:
    for i in result1:
        print(i)





