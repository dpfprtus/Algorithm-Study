n = int(input())
number =[]
for x in range(n):
    number.append(int(input()))
number.sort()
for i in number:
    print(i,end=' ')