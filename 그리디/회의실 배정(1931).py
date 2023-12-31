n = int(input())
info = [list(map(int,input().split())) for _ in range(n)]
info.sort(key = lambda x: (x[1],x[0]))
cnt = 1
last_end = info[0][1]
for i in range(1,len(info)):
    start,end = info[i]
    if last_end > start:
        continue
    else:
        last_end = end
        cnt += 1
print(cnt)


