import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == ".":
        break
    s = s.replace(" ","")
    stack = []
    flag = 0
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = 1
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = 1
                break
    if stack or flag == 1:
        print("no")
    else:
        print("yes")
    