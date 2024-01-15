import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
s.sort(key=lambda x : x[0])
s_sum = 0
for i in range(n):
    s_sum += s[i][1]

result = 0
for i in range(n):
    result += s[i][1]
    if result >= s_sum/2:
        print(s[i][0])
        break