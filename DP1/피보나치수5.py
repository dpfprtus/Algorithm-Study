n = int(input())
result = 0
def fibo(s):
    a = 1
    b = 1
    if n ==1 or n == 2:
        return 1
    for i in range(1,n):
        a,b = b,a+b
    return a
if n == 0:
    print(0)
else:
    print(fibo(n))