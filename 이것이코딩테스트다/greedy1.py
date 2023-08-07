n,m = map(int,input().split())

list1 = []

for x in range(n):
    k = list(map(int, input().split()))
    k.sort()
    list1.append(k)
list1.sort()
result = list1[-1][0] 
print(result)
