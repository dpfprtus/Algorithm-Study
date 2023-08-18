n = input()
priority = {"*":3,"/":3,"+":2,"-":2,"(":1,")":1}
stack = []
result = []

for i in n:
    if i == "(":
        stack.append(i)
    elif i in "*/+-":
        if not stack:
            stack.append(i)
        else:
            while priority[stack[-1]] >= priority[i]:
                tmp = stack.pop()
                result.append(tmp)
                if not stack:
                    break
            stack.append(i)
    elif i == ")":
        tmp = stack.pop()
        while tmp != "(":
            result.append(tmp)
            tmp = stack.pop()
    else:
        result.append(i)
while stack:
    result.append(stack.pop())
print(''.join(result))
        