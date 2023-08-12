
num = int(input())
sick = input()
num_list = [int(input()) for _ in range(num)]
stack = []
cnt = 0
alphabet = []

for i in sick:
    if i != "*" and i != "+" and i != "/" and i != "-":
         if i not in alphabet:
             alphabet.append(i)
             
mapping = {}
for k in range(len(alphabet)):
    mapping[alphabet[k]] = num_list[k]

for i in sick:
    if i != "*" and i != "+" and i != "/" and i != "-":
         stack.append(mapping[i])
         cnt += 1
    else:
        if i == "*":
            a = stack.pop() * stack.pop()
            stack.append(a)
   
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(round(float(b/a),2))
        elif i == "+":
            a = stack.pop() + stack.pop()
            stack.append(a)
      
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        
print("{:.2f}".format(stack.pop()))
