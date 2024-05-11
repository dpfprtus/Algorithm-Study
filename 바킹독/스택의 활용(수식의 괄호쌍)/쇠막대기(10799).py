s = input()
stack = ["("]
result = 0

for i in range(1,len(s)):
    if s[i] == "(":
        stack.append(i)
    else:
        if stack:
            if s[i-1] == "(":
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1
print(result)