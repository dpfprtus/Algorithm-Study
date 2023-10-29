n,b = input().split(" ")
n = ''.join(reversed(n))
b = int(b)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0
for i in range(len(n)-1,-1,-1):
    sum = number.index(n[i]) * (b**i)
    result += sum
print(result)