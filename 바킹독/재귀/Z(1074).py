N,r,c = map(int,input().split())

def func(n,r,c):
    if n == 0:
        return 0
    
    count = 2*(r%2) + c % 2
    return 4 * func(n-1,r//2,c//2) + count

print(func(N,r,c))