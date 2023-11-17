a,b = map(int,input().split())

def gcd(a,b):
    if a > b:
        while(b > 0):
            a ,b = b, a%b
        return a
    else:
        while(a > 0):
            b,a = a, b %a
        return b

print(gcd(a,b))
print(int(a*b / gcd(a,b)))

