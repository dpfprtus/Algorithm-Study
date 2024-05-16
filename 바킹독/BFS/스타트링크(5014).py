from collections import deque

F,S,G,U,D = map(int,input().split())

def bfs():

    while q:
        x = q.popleft()

        for i in range(2):
            nx = x + dx[i]

            if 1<= nx <= F and visit[nx] == 0 and nx != S:
                if nx == G:
                    return visit[x]+1
                visit[nx] = visit[x]+1
                q.append(nx)
    return "use the stairs"

dx = [U,-D]
visit = [0]*1000002
q = deque([S])

if S==G:
    print(0)
else:
    print(bfs())


        