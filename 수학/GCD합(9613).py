from itertools import combinations

t = int(input())

def gcd(a,b):
    if a > b:
        while(b>0):
            a,b = b, a%b
        return a
    else:
        while(a>0):
            b,a = a, b%a
        return b

for i in range(t):
    gcds = list(map(int,input().split()))
    comb = list(combinations(gcds[1:],2))
    result = []
    for a,b in comb:
        result.append(gcd(a,b))
    print(sum(result))