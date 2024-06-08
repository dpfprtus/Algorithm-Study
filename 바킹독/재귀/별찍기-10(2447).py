n = int(input())

maps = [[' ']*n for _ in range(n)]

def fucn(n,x,y):
    
    if n == 1:
        maps[x][y] = "*"
        return
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            fucn(int(n/3),x+int(n/3)*i,y+int(n/3)*j)

fucn(n,0,0)
for i in maps:
    print(''.join(i))
        