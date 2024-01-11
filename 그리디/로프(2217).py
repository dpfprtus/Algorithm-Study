n = int(input())
weight = [int(input()) for _ in range(n)]
result = []

weight.sort()
for i in range(n):
    result.append(weight[i]*n)
    n -= 1
print(max(result))

