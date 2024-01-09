import sys
input = sys.stdin.readline
#n=마을수, c=트럭 용량
n,c = map(int,input().split())
m = int(input())
boxs = [list(map(int,input().split())) for _ in range(m)]
boxs.sort(key=lambda x:(x[1]))
result = 0

box = [c]*(n+1)
_min = 0
for s,e,b in boxs:
    _min = c
    for i in range(e,b):
        _min = min(_min,box[i])
    _min = min(_min,b)

    for i in range(e,b):
        box[i] -= _min
    result += _min
print(result)