t = int(input())

def sosu(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for _ in range(t):
    n = int(input())
    while(True):
        if n == 0 or n == 1:
            print(2)
            break
        if sosu(n):
            print(n)
            break
        n += 1
        if n == 4000000000:
            break
