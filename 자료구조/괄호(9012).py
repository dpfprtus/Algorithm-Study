#1회 다시품
import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    stack = []
    s = input()
    flag = 0
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                flag = 1
                break
    if stack:
        print("NO")
    elif not stack and flag == 0:
        print("YES")
