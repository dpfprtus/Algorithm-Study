n = int(input())

def func(cur):

    global cnt,n

    if cur == n:
        cnt += 1
        return
    
    for i in range(n):
        if not init1[i] and not init2[cur+i] and not init3[cur-i+n-1]:
            init1[i] = 1
            init2[i+cur] = 1
            init3[cur-i+n-1] = 1
            func(cur+1)
            init1[i] = 0
            init2[i+cur] = 0
            init3[cur-i+n-1] = 0

init1 = [0]*40
init2 = [0]*40
init3 = [0]*40
cnt = 0
func(0)
print(cnt)