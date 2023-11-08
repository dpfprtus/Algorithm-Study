n = int(input())
a = n
while(a != 1):
    for i in range(2,n+1):
        if a % i == 0:
            print(i)
            a = int(a//i)
            break