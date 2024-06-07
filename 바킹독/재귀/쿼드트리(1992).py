n = int(input())
video = [input() for _ in range(n)]

def check(x,y,z):
    for i in range(x,x+z):
        for j in range(y,y+z):
            if video[x][y] != video[i][j]:
                return False
    return True

def func(x,y,z):

    if check(x,y,z):
        print(video[x][y],end="")
        return
    
    print("(",end="")
    
    n = z // 2
    for i in range(2):
        for j in range(2):
            func(x+n*i,y+n*j,n)

    print(")",end="")

func(0,0,n)
