n,m,k = map(int,input().split())
note = [[0]*m for _ in range(n)]
stickers = []

#회전 하기
def rotate(a):
    result = zip(*a[::-1])
    return [list(e) for e in result]

#노트북에 붙일 수 있는지 검증하고 붙이기
def note_stick(x,y,sticker,r,c):

    if len(sticker) > n or len(sticker[0]) > m:
        return False
    
    for i in range(r):
        for j in range(c):
            if note[x+i][y+j] == 1 and sticker[i][j] == 1:
                return False
    
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                note[x+i][y+j] = 1

    return True

def rotate_stick(sticker):

    for _ in range(4):
        r = len(sticker)
        c = len(sticker[0])
        for i in range(n-r+1):
            for j in range(m-c+1):
                if note_stick(i,j,sticker,r,c):
                    return
        sticker = rotate(sticker)
    return 

def result():
    result = 0
    for i in range(n):
        for j in range(m):
            if note[i][j] == 1:
               result += 1
    return result          
     
for _ in range(k):
    r,c = map(int,input().split())
    stick = [list(map(int,input().split())) for _ in range(r)]
    rotate_stick(stick)

print(result())



        