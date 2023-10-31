a,b,c,m = map(int,input().split())
time = 0
piro = 0
result = 0
for i in range(1, 25):
    if a > m:
        break
    if piro+a <= m:
        piro += a
        time += b
    else:
        piro -= c
        if piro <= 0:
            piro = 0

print(time)