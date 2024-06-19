n,m,x,y,k = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
orders = list(map(int,input().split()))

#이동 명령
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

dice =[[0]*3 for _ in range(4)]

dice_x = x
dice_y = y

def move(x,y,idx):

    global dice_x
    global dice_y

    dice_x = x + dx[idx]
    dice_y = y + dy[idx]
    
    if dice_x < 0 or dice_y < 0 or dice_x >= n or dice_y >= m:
        dice_x = x
        dice_y = y
        return False
    
    if idx == 1:
        left = dice[1][0]
        right = dice[1][2]
        second = dice[1][1]
        fourth = dice[3][1]

        dice[1][1] = left
        dice[1][0] = fourth
        dice[1][2] = second
        dice[3][1] = right

    elif idx == 2:
        left = dice[1][0]
        right = dice[1][2]
        second = dice[1][1]
        fourth = dice[3][1]

        dice[1][1] = right
        dice[1][0] = second
        dice[1][2] = fourth
        dice[3][1] = left
    
    elif idx == 3:
        first = dice[0][1]
        second = dice[1][1]
        third = dice[2][1]
        fourth = dice[3][1]
        dice[0][1] = second
        dice[1][1] = third
        dice[2][1] = fourth
        dice[3][1] = first
    
    elif idx == 4:
        first = dice[0][1]
        second = dice[1][1]
        third = dice[2][1]
        fourth = dice[3][1]
        dice[0][1] = fourth
        dice[1][1] = first
        dice[2][1] = second
        dice[3][1] = third

    if maps[dice_x][dice_y] != 0:

        dice[3][1] = maps[dice_x][dice_y]
        maps[dice_x][dice_y] = 0
    else:
        maps[dice_x][dice_y] = dice[3][1]

    return True
#order에 따라 주사위를 회전

for order in orders:
    if move(dice_x,dice_y,order):
        print(dice[1][1])
