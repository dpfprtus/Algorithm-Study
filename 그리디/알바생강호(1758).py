import sys
input = sys.stdin.readline

n = int(input())
price = [int(input()) for _ in range(n)]
price.sort(reverse=True)
result = []
tip = 0
for i in range(len(price)):
    tip = price[i] - i
    if tip < 0:
        continue
    result.append(tip)
print(sum(result))
