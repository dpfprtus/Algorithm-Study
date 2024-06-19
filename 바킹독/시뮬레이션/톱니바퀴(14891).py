import sys
from collections import deque
input = sys.stdin.readline

chain = [list(map(int,input().rstrip())) for _ in range(4)]

#N = 0, S = 1
#시계방향 = 1, 반시계 = -1
k = int(input())

do = []
chain2 = []

for _ in range(k):
    a,b = map(int,input().split())
    a -= 1
    do.append([a,b])

#최종 톱니바퀴 점수 계산
def cal():
    return sum(chain[i][0] * (2**i) for i in range(4))

#개별 톱니바퀴 회전

def chain_rotate(x,y):
    chain2 = deque(chain[x])
    chain2.rotate(y)
    chain[x] = list(chain2)
    return

#톱니바퀴 회전
def spin(x,y):
  
    tmp = []

    for i in range(3):
        tmp.append([chain[i][2],chain[i+1][6]])
    chain_rotate(x,y)
    
    flag = 0

    if x == 0:
        a,b = tmp[0]
        if a != b:
            flag = 1
            chain_rotate(1,-y)
        a,b = tmp[1]
        if a!= b and flag == 1:
            chain_rotate(2,y)
        else:
            flag = 0
        a,b = tmp[2]
        if a!= b and flag == 1:
            chain_rotate(3,-y)

    elif x == 1:
        a,b = tmp[0]
        if a != b:
            chain_rotate(0,-y)
        a,b = tmp[1]
        if a != b:
            flag = 1
            chain_rotate(2,-y)
        a,b = tmp[2]
        if a != b and flag == 1:
            chain_rotate(3,y)
    
    elif x == 2:
        a,b = tmp[1]
        if a!=b:
            flag = 1
            chain_rotate(1,-y)
            
        a,b = tmp[0]
        if a!=b and flag == 1:
            chain_rotate(0,y)
        
        a,b = tmp[2]
        if a!= b:
            chain_rotate(3,-y)

    elif x == 3:
        a,b = tmp[2]
        if a!= b:
            flag = 1
            chain_rotate(2,-y)
        a,b = tmp[1]
        if a!=b and flag == 1:
            chain_rotate(1,y)
        else:
            flag = 0
        a,b = tmp[0]
        if a!=b and flag == 1:
            chain_rotate(0,-y) 
    return

for x,y in do:
    spin(x,y)

print(cal())
