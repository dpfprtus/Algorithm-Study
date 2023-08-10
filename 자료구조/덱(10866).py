from collections import deque
from sys import stdin

num = int(input())
result = deque()

for _ in range(num):
    a = stdin.readline().rstrip().split()
    if a[0] == "push_front":
        result.appendleft(int(a[1]))
    elif a[0] == 'push_back':
        result.append(int(a[1]))
    elif a[0] == 'pop_front':
        if result:
            print(result.popleft())
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if result:
            print(result.pop())
        else:
            print(-1)
    elif a[0] == "size":
        print(len(result))
    elif a[0] == "empty":
        if result:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if result:
            print(result[0])
        else:
            print(-1)
    elif a[0] == "back":
        if result:
            print(result[-1])
        else:
            print(-1)
