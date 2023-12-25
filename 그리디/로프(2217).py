import sys
input = sys.stdin.readline
n = int(input())
lope = [int(input()) for _ in range(n)]
result = []
lope.sort()

for x in lope:
    result.append(x*n)
    n -= 1
print(max(result))