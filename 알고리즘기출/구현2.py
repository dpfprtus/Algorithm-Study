s = input()

number = ['0','1','2','3','4','5','6','7','8','9']
sum = 0
alpha = []
for x in range(len(s)):
    if s[x] in number:
        sum += int(s[x])
    else:
        alpha.append(s[x])
alpha.sort()
result = ""
for x in alpha:
    result += x
if sum != 0:
    print(result+str(sum))
else:
    print(result)