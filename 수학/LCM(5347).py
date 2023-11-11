n = int(input())
def gcd(a,b):
    if a>b:
        while(b > 0):
            a,b = b, a%b
        return a
    else:
        while(a > 0):
            b,a = a, b%a
        return b
for _ in range(n):
    a,b = map(int,input().split())
    print(int(a*b / gcd(a,b)))