n = int(input())
a = list(map(int,input().split()))
x = int(input())
result = []
def gcd(a,b):
    if a>b:
        while(b > 0):
            a,b = b,a%b
        return a
    else:
        while(a>0):
            b,a = a,b%a
        return b
for i in a:
    if gcd(i,x) == 1:
        result.append(i)

print(sum(result)/len(result))