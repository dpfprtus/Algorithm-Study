a,b = input().split(' ')
cnt = 1
while(True):
    if int(a) == int(b):
        print(cnt)
        break
    elif int(a) > int(b):
        print(-1)
        break
    elif b[-1] == "1":
        b = b[:-1]
        cnt += 1
        continue
    elif int(b[-1]) % 2 == 0:
        b = str(int(b) // 2)
        cnt += 1
        continue
    print(-1)
    break
    