n = int(input())
maps = [[' ']*(n*2-1) for _ in range(n)]

def fill(x,y):
    maps[x][y] = "*"
    maps[x+1][y-1] = "*"
    maps[x+1][y+1] = "*"
    
    for i in range(y-2,y+3):
        maps[x+2][i] = "*"
    
def func(x,y,n):
    
    if n == 3:
        fill(x,y)
        return
    
    ns = int(n / 2)
    func(x,y,ns)
    func(x+ns,y-ns,ns)
    func(x+ns,y+ns,ns)
            
 
func(0,n-1,n)

for i in maps:
    print(''.join(i))