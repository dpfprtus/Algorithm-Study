from sys import stdin

n,m = map(int,input().split())
a = []
result = 0
for _ in range(n):
    a.append(stdin.readline().rstrip())
for _ in range(m):
    b = stdin.readline().rstrip()
    if b in a:
        result+=1
print(result) 