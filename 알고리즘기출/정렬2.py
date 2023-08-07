n = int(input())
house = list(map(int,input().split()))
result_sum = 0
result = []
for i in range(n):
    for j in range(n):
        result_sum += abs(house[i]-house[j])
    result.append((result_sum,house[i]))
    result_sum = 0
result.sort(key=lambda x:x[0])
print(result[0][1])