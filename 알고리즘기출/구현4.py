from itertools import combinations
n,m = map(int,input().split())

data = []

for _ in range(n):
    data.append(list(map(int,input().split())))

houses = []
chicken = []
for x in range(n):
    for j in range(n):
        if data[x][j] == 1:
            houses.append([x,j])
        if data[x][j] == 2:
            chicken.append([x,j])
chicken_road = list(combinations(chicken, m))
result = []
last_result = []
temp = 1e9
print(chicken_road)
for roads in chicken_road:
    for house in houses:
        x,k = house
        for road in roads:
            a,b = road
            start = min(temp,abs(x-a) + abs(k-b))
            temp = start
        result.append(start)
        temp = 1e9
    last_result.append(sum(result))
    result = []
print(min(last_result))