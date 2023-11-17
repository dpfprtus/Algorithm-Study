from itertools import combinations
s = list(input())
idx = []
idx2 = []
for i in range(len(s)):
    if s[i] == "(":
        idx.append(i)
    elif s[i] == ")":
        idx2.append(i)
idx3 =[]
idx2.reverse()
for i in range(len(idx)):
    idx3.append((idx[i],idx2[i]))
idx3.reverse()
print(idx3)
for a,b in idx3:
    print(a,b)
    c = s
    c.remove(a)
    c.remove
    print(''.join(c))