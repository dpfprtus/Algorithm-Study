n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

def rotate(board):
    tmp = zip(*board[::-1])
    return [list(i) for i in tmp]

def move(board2,idx):
    
    tmp = [[0]*n for _ in range(n)]

    if idx == 2:
        board2 = rotate(board2)
    elif idx == 3:
        board2 = rotate(board2)
        board2 = rotate(board2)
    elif idx == 4:
        board2 = rotate(board2)
        board2 = rotate(board2)
        board2 = rotate(board2)

    for i in range(n):
        cnt = 0
        for j in range(n):
            if board2[i][j] == 0:
                continue

            if tmp[i][cnt] == 0:
                tmp[i][cnt] = board2[i][j]

            elif board2[i][j] == tmp[i][cnt]:
                tmp[i][cnt] *= 2
                cnt += 1
            else:
                cnt += 1
                tmp[i][cnt] = board2[i][j]
    
    if idx == 4:
        tmp = rotate(tmp)
    elif idx == 3:
        tmp = rotate(tmp)
        tmp = rotate(tmp)
    elif idx == 2:
        tmp = rotate(tmp)
        tmp = rotate(tmp)
        tmp = rotate(tmp)
    
    return tmp

ans = [0]*5
answer = 0

def func(k):
    global answer
    if k == 5:
        board2 = [[j for j in board[i]] for i in range(n)]
        for i in range(5):
            board2 = move(board2,ans[i])

        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result,board2[i][j])
        answer = max(answer,result)
        return
    
    for i in range(1,5):
        ans[k] = i
        func(k+1)

func(0)
print(answer)