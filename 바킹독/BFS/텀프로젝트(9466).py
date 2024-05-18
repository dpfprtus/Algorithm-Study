from collections import deque

def bfs(key):
    cur = key

    while True:
        visit[cur] = key
        cur = students[cur]

        if visit[cur] == key:
            while visit[cur] != "CYCLE_IN":
                visit[cur] = "CYCLE_IN"
                cur = students[cur]
            return
        
        elif visit[cur] != 0:
            return

           

for _ in range(int(input())):
    n = int(input())

    students = [0]+list(map(int,input().split()))

    visit = [0]*(n+1)
    cnt = 0
    for i in range(1,n+1):
        if visit[i] == 0:
            bfs(i)

    for i in range(1,n+1):
        if visit[i] != "CYCLE_IN":
            cnt += 1

    print(cnt)


