n = int(input())
yang = list(map(int,input().split()))
yang.sort()
result = yang[-1]
for i in range(len(yang)-1):
    result += yang[i]/2
print(result)
