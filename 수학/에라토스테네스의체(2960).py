n,k = map(int,input().split())
cnt = 0
chae = [i for i in range(2,n+1)]

while chae:
    max_num = max(chae)
    min_num = min(chae)
    num = min_num
    chae.remove(num)
    cnt += 1
    if cnt == k:
        print(num)
        break
    while(num < max_num):
        num = num + min_num
        if num in chae:
            chae.remove(num)
            cnt += 1
        if cnt == k:
            print(num)
            break
    

        
        