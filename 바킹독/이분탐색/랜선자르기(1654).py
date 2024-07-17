import sys
input = sys.stdin.readline

k,n = map(int,input().split())
lan = [int(input()) for _ in range(k)]
st,en = 1,max(lan)

def solve(x):
    cur = 0
    for i in lan:
        cur += i // x
    return cur >= n

while st <= en:
    mid = (st+en) // 2
    if solve(mid):
        st = mid+1
    else:
        en = mid-1
print(en)



