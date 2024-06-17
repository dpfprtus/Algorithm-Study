import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
city = []
chicken = []

for i in range(n):
    city.append(list(map(int,input().split())))
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))

chicken_cnt = len(chicken)

def cal(x,y,city):
    result = 200
    for i in range(n):
        for j in range(n):
            if city[i][j] == 2:
                result = min(result,abs(x-i)+abs(y-j))
    return result

result = float("inf")

for remove_chicken in combinations(chicken,chicken_cnt-m):
    city2 = [[j for j in city[i]] for i in range(n)]

    for x,y in remove_chicken:
        city2[x][y] = 0
        
    chicken_road = 0

    for i in range(n):
        for j in range(n):
            if city2[i][j] == 1:
                chicken_road += cal(i,j,city2)
    result = min(result,chicken_road)

print(result)
