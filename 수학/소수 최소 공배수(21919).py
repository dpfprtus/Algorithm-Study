import sys
n = int(input())
a = list(map(int,input().split()))

def sosu(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def gcd(a,b):
    if a > b:
        while b >0:
            a,b = b,a%b
        return a
    else:
        while a>0:
            b,a = a,b%a
        return b

sosu_list = []

for i in a:
    if sosu(i):
        sosu_list.append(i)
sosu_list = set(sosu_list)
sosu_list = list(sosu_list)
if len(sosu_list) == 0:
    print(-1)
else:
    result = 1
    for i in sosu_list:
        result *= i
    print(result)