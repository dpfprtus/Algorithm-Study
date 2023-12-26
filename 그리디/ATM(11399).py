n = int(input())
time = list(map(int,input().split()))

time.sort()
result = []
time_sum = 0
for i in time:
    time_sum += i 
    result.append(time_sum)
print(sum(result))