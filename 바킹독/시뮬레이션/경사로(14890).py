import sys
input = sys.stdin.readline

N,L = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
result = 0

def maps_rotate():
    global maps
    tmp = zip(*maps[::-1])
    maps = [list(e) for e in tmp]

def check(tmp):
    visited = [0]*N
    for i in range(N-1):
        a = abs(tmp[i] - tmp[i+1]) 
        if a > 1:
            return False
        elif a == 1:
            if i-L+1 >= 0 and tmp[i] < tmp[i+1]:
                if 1 in visited[i-L+1:i+1]:
                    return False
                if check_L(tmp[i-L+1:i+2],"back"):
                    visited[i-L] = 1
                    continue
                else:
                    return False
            elif i+L < N and tmp[i] > tmp[i+1]:
                if 1 in visited[i+1:i+L]:
                    return False
                if check_L(tmp[i:i+L+1],"front"):
                    visited[i+L] = 1
                    continue
                else:
                    return False
            return False
    return True

def check_L(tmp,point):
    first = tmp[0]
    second = tmp[-1]
    cnt = 0
    if point == "front":
        for i in range(1,L+1):
            a = abs(first-tmp[i])
            if a == 1:
                cnt += 1
    else:
        for i in range(L):
            a = abs(second-tmp[i])
            if a == 1:
                cnt += 1

    if cnt == L:
 
        return True
    return False


for i in range(N):
    if check(maps[i]):
     
        result+=1

maps_rotate()
for i in range(N):
    if check(maps[i]):
  
        result+=1
print(result)