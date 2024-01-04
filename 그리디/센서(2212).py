import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
position = list(map(int,input().split()))
position.sort()
ans = []

for i in range(n-1):
    ans.append(position[i+1]-position[i])
ans.sort()
print(sum(ans[:n-k]))

