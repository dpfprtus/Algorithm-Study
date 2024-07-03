n = int(input())
room = [list(map(int,input().split(" "))) for _ in range(n)]

room.sort(key=lambda x:(x[1],x[0]))
result = 1
last = room[0][1]
for i in range(n-1):
    if last <= room[i+1][0]:
        result += 1
        last = room[i+1][1]

print(result)