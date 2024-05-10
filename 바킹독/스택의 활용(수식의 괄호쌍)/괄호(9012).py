import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    s = input().rstrip()
    stack = []
    flag = 0

    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = 1
    if stack or flag == 1:
        print("NO")
    else:
        print("YES")