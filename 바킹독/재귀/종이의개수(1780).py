n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
cnt = [0,0,0]

def check(x,y,z):
    for i in range(x,x+z):
        for j in range(y,y+z):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def func(x,y,z):
    
    if check(x,y,z):
        cnt[paper[x][y]+1] += 1
        return

    n = int(z / 3)
    for i in range(3):
        for j in range(3):
            func(x+n*i,y+n*j, n)

func(0,0,n)
print(*cnt,sep="\n")