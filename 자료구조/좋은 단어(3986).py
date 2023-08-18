from sys import stdin

n = int(input())

cnt = 0
for _ in range(n):
    a = stdin.readline().rstrip()
    stack = []
    for i in a:
        if not stack:
            stack.append(i)
            continue
        if i == "A":
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

        elif i == "B":
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if not stack:
        cnt += 1
print(cnt)   