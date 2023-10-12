from sys import stdin
input = stdin.readline
n = int(input())

if n == 2:
    a,b = map(int,input().split())
    min = min(a,b)
    for i in range(1,min+1):
        if a % i == 0 and b % i == 0:
            print(i)
if n == 3:
    a,b,c = map(int,input().split())
    min = min(a,b,c)
    for i in range(1,min+1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            print(i)           
