n = int(input())
office = [list(map(int,input().split())) for _ in range(n)]

office.sort(key=lambda x:x[0])
sum_people = 0
for i in range(n):
    sum_people += office[i][1]
people = 0
for i in range(n):
    people += office[i][1]
    if people >= sum_people/2:
        print(office[i][0])
        break

