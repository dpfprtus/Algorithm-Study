#다시품
from itertools import combinations

s = list(input())
stack = []
index = []

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    elif s[i] == ")":
        index.append((stack.pop(),i))
result = set()  
for i in range(1,len(index)+1):
    a = list(combinations(index,i))
    for b in a:
        temp = s[:]
        for c,d in b:  
            temp[c] = ''
            temp[d] = ''
        result.add(''.join(temp))
result = list(result)
result.sort()
for i in result:
    print(i)