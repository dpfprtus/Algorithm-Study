n,m = map(int,input().split())
gong = list(map(int,input().split()))
count = 0

for x in range(len(gong)-1):
    for j in range(x+1,len(gong)):
        if gong[x] != gong[j]:
            count+=1
print(count)