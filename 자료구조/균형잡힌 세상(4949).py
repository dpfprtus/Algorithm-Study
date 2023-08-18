from sys import stdin

while True:
    b = stdin.readline()
    a = b.replace(" ","")
    stack = []
    flag = 0
    if b[0] == ".":
        break
    for i in a:
        if i =="(":
            stack.append(i)
        elif i=="[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] != "[":
                stack.pop()
            else:
                flag = 1
                break
        elif i == "]":
            if stack and stack[-1] != "(":
                stack.pop()
            else:
                flag = 1
                break
    if stack or flag:
        print("no")
    else:
        print("yes")      