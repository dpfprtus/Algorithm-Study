import sys
input = sys.stdin.readline

n = int(input())
s = [0]
result = []
num = 0
flag = 0
for _ in range(n):
    a = int(input())
    if s[-1] < a:
        last = s[-1]
        for i in range(num+1,a+1):
            s.append(i)
            num += 1
            result.append("+")
    if s[-1] == a:
        s.pop()
        result.append("-")
        continue
    else:
        flag = 1
        break

if flag == 1:
    print("NO")            
else:
    for i in range(len(result)):
        print(result[i])
