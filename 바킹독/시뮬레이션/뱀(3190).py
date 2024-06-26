import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

maps = [[0]*(n) for _ in range(n)]

for _ in range(k):
    x,y = map(int,input().split())
    maps[x-1][y-1] = "apple"

L = int(input())

direction = []
for _ in range(L):
    x,y = input().split()
    direction.append([int(x),y])

snake = deque([[0,0]])
time = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
#0은 동쪽, 1은 남쪽, 2는 서쪽 , 3은 북쪽
now_dir = 0

#뱀의 머리
x,y = 0,0

while True:

    time += 1

    x += dx[now_dir]
    y += dy[now_dir]

    if x < 0 or y < 0 or x>=n or y>=n or [x,y] in snake:
        break

    snake.append([x,y])

    if maps[x][y] != 'apple':
        snake.popleft()
    #사과를 무한으로 먹이고 있었다...문제를 좀 더 꼼꼼히 읽자.
    else:
        maps[x][y] = 0
    
    for i in range(L):
        if direction[i][0] == time:
            if direction[i][1] == "L":
                now_dir = (now_dir +3) % 4
            else:
                now_dir = (now_dir+1) % 4
 
print(time)