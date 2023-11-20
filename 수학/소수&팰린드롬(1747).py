import sys
input = sys.stdin.readline

def sosu(num):
    #소수 찾기
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def rev(str):
    reversed_str = ''
    for c in str:
        reversed_str = c + reversed_str
    return reversed_str


n = int(input())

while True:
    sosu1 = rev(str(n))
    if n == 1:
        print(2)
        break
    if str(n) == sosu1 and sosu(n):
        print(n)
        break
    n += 1
