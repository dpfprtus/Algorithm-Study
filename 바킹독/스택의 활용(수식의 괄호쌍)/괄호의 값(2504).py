s = input()
stack = []
result = 0
tmp = 1

for i in range(len(s)):
    if s[i] == "(":
        tmp *= 2
        stack.append(s[i])
    elif s[i] == "[":
        tmp *= 3
        stack.append(s[i])
    elif s[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if s[i-1] == "(":
            result += tmp
        stack.pop()
        tmp //= 2
    elif s[i] == "]":
        if not stack or stack[-1] == "(":
            result = 0
            break
        if s[i-1] == "[":
            result += tmp
        stack.pop()
        tmp //= 3
if stack:
    print(0)
else:
    print(result)
    