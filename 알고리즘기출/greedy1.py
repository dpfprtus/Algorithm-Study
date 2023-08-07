n = int(input())
datas = list(map(int,input().split()))

datas.sort(reverse=True)
result = []
count = 0
for data in datas:
    result.append(data)
    if len(result) == result[0]:
        count += 1
        result = []

print(count)