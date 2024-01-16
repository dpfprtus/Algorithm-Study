n = int(input())

def fibo(s):
    a = 1
    b = 1
    if s == 1 or s == 2:
        return 1
    for i in range(1,n):
        a,b = b,a+b
    return a
print(fibo(n))