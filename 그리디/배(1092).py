import sys
input = sys.stdin.readline

n = int(input())
crain_kg = list(map(int,input().split()))
box = int(input())
box_kg = list(map(int,input().split()))
time = 0

crain_kg.sort(reverse=True)
box_kg.sort(reverse=True)

if crain_kg[0] < box_kg[0]:
    print(-1)
else:
    while box_kg:
        if not box_kg:
            break
        for crain in crain_kg:
            for box in box_kg:
                if crain >= box:
                    box_kg.remove(box)
                    break
        time += 1
    print(time)


