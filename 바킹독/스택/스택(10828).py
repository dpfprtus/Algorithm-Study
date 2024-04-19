import sys
input = sys.stdin.readline
n = int(input())
s = []
for _ in range(n):
    a = input().split()
    
    if a[0] == 'push':
        s.append(int(a[1]))
    elif a[0] == "top":
        if s:
            print(s[-1])
        else:
            print(-1)
    elif a[0] == "size":
        print(len(s))
    elif a[0] == "pop":
        if s:
            print(s.pop())
        else:
            print(-1)
    elif a[0] == "empty":
        if s:
            print(0)
        else:
            print(1)
