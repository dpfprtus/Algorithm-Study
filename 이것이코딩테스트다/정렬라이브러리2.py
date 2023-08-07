student = int(input())

info = []

for x in range(student):
    a,b = input().split()
    b = int(b)
    info.append([a,b])

info.sort(key=lambda x:x[1])

for a,b in info:
    print(a, end=' ')