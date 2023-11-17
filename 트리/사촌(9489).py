from collections import deque

tree = [[] for _ in range(1000001)]
while True:
    try:
        n,k = map(int,input().split())
        if n == 0 and k == 0:
            break
        num = deque(map(int,input().split()))
        root = num.popleft()
        while num:
            last = num.popleft()
            if num[0] - last == 1:
                tree[root].append(last)

    except:
        break