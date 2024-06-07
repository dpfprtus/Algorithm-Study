n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
cnt = [0,0]

def check(x,y,z):
    for i in range(x,x+z):
        for j in range(y,y+z):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def func(x,y,z):

    if check(x,y,z):
        cnt[paper[x][y]] += 1
        return
    
    n = z // 2
    for i in range(2):
        for j in range(2):
            func(x+i*n,y+j*n,n)

func(0,0,n)
print(*cnt,sep="\n")