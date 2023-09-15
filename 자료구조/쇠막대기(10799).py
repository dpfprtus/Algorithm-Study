import sys
input = sys.stdin.readline

stack = []
result = 0
tmp = 0
s = input()

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    elif s[i] == ")":
        
        if s[i-1] == "(":
            stack.pop()
            result += len(stack)
        else:
            result += 1
            stack.pop()
print(result)
        
        