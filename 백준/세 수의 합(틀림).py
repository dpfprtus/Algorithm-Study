#시간 초과때문에 조합 or 삼중for문 사용이 안댐 따라서 a+b = d-c를 이용
n = int(input())
data = set()
for i in range(n):
    data.add(int(input()))

ans = set()
for i in data:
    for j in data:
        ans.add(i+j)
result = {}
for i in data:
    for j in data:
        if i-j in ans:
            result[i] = (i,j,i-j)
key = list(result.keys())
key.sort(reverse=True)
print(key[0])