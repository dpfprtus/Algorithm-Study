import sys
input = sys.stdin.readline

s = list(input().rstrip())
s2 = []
m = int(input())
for _ in range(m):
    a = list(input().split())
    if a[0] == "L":
        if s:
            s2.append(s.pop())
    elif a[0] == "D":
        if s2:
            s.append(s2.pop())
    elif a[0] == "B":
        if s:
         s.pop()
    elif a[0] == "P":
        s.append(a[1])
s.extend(reversed(s2))
print(''.join(s))


