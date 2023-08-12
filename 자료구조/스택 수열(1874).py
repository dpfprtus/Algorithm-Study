n = int(input())

stack = []
result = []
cur = 1
flag = 0
for _ in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur +=1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else: #stack의 맨윗값이 num과 일치하지 않으면 수열을 만들 수 없다.
        #왜냐하면 stack은 오름차순이기에 num값이 stack 맨위보다 아래에 있기 때문이다.
        print("NO")
        flag = 1
        break

if not flag:
    for i in result:
        print(i)

    