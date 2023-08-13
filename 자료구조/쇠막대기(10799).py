a = input()
stack = []
result = 0
for i in range(len(a)):
    if a[i] == "(":
        stack.append(i)
    elif a[i] == ")":
        if a[i-1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop() #))이런식이면 1만 추가하면된다.
            result += 1
            
print(result)
            
    