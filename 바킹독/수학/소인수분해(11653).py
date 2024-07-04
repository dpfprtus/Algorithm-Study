n = int(input())

result = []

while n != 1:
    for i in range(2,int(n**0.5)+1):
        while n % i == 0:
            result.append(i)
            n //= i
    if n != 1:
        result.append(n)
        n = 1
for i in result:
    print(i)