import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
honey = list(map(int,input().split()))
honey_two = deepcopy(honey)
for i in range(1,n):
    honey_two[i] += honey_two[i-1]
result = 0

for i in range(1,n-1):
    result = max(result,honey_two[-1]*2-honey_two[i]-honey[i]-honey[0])
for i in range(1,n-1):
    result = max(result,honey_two[i-1]+honey_two[-1]-honey[i]-honey[-1])
for i in range(1,n-1):
    result = max(result,honey_two[-1]-honey_two[i-1]+honey_two[i]-honey[0]-honey[-1])
print(result)
