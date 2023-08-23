from sys import stdin
n,m = map(int,input().split())
pocketmon = {}
pocketmon2 = {}
for i in range(n):
    a = stdin.readline().rstrip()
    temp = {i:a}
    temp2 = {a:i}
    pocketmon.update(temp)
    pocketmon2.update(temp2)

for _ in range(m):
    a = stdin.readline().rstrip()
    if a[0] in '0123456789':
        a = int(a)
        print(pocketmon.get(a-1))
    else:
        print(pocketmon2.get(a)+1)

    

    