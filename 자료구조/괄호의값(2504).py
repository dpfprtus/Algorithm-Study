import sys
input = sys.stdin.readline

s = list(input())
result = 0
stack = [] 
tmp = 1
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
        tmp *= 2
    elif s[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        else:
            if s[i-1] =="(":
                result += tmp
            stack.pop()
            tmp //= 2
    elif s[i] == "[":
        stack.append(s[i])
        tmp *= 3
    elif s[i] == "]":
        if not stack or stack[-1] == "(":
            result = 0
            break
        else:
            if s[i-1] =="[":
                result += tmp
            stack.pop()
            tmp //= 3
if stack:
    print(0)
else:
    print(result)

 
    