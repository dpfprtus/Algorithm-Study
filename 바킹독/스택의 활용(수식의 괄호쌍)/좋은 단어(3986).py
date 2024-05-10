import sys
input = sys.stdin.readline
n = int(input())
result = 0

for _ in range(n):
    s = input().rstrip()
    stack = []
    
    for i in s:

        if i == "A":
            if stack and stack[-1] == "A":
                stack.pop()
            else:
                stack.append(i)
        elif i == "B":
            if stack and stack[-1] == "B":
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        result += 1
print(result)
