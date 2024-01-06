import sys
input = sys.stdin.readline
n = int(input())
towns = [list(map(int,input().split())) for _ in range(n)]
sum_people = 0
result = 0
for i in range(len(towns)):
    sum_people += towns[i][1]

towns.sort(key=lambda x:x[0])
for i in range(len(towns)):
    result += towns[i][1]
    if result >= sum_people/2:
        print(towns[i][0])
        break