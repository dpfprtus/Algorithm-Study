import sys
input = sys.stdin.readline

n = int(input())
crain = list(map(int,input().split()))
m = int(input())
boxs = list(map(int,input().split()))
crain.sort(reverse=True)
boxs.sort(reverse=True)
time = 0
if crain[0] < boxs[0]:
    print(-1)
else:
    while boxs:
        if not boxs:
            break
        for i in crain:
            for box in boxs:
                if i >= box:
                    boxs.remove(box)
                    break
        time += 1
    print(time)