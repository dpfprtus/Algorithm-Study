import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

point = list(map(int,input().split()))
point.sort()
ans = []
for i in range(n-1):
    ans.append(abs(point[i+1]-point[i]))
ans.sort()
print(sum(ans[:n-k]))