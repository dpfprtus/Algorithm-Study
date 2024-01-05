from copy import deepcopy

n = int(input())
honey = list(map(int,input().split()))
sum_honey = deepcopy(honey)
result = 0

for i in range(1,n):
    sum_honey[i] += sum_honey[i-1]

for i in range(1,n-1):
    result = max(result,2*sum_honey[-1]-honey[0]-honey[i]-sum_honey[i])

for i in range(1,n-1):
    result = max(result,sum_honey[-1]-honey[-1]+sum_honey[i-1]-honey[i])

for i in range(1,n-1):
    result = max(result,sum_honey[i]-honey[0]+sum_honey[-1]-sum_honey[i-1]-honey[-1])
print(result)
