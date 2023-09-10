from collections import deque,defaultdict

while True:

    n,k = map(int,input().split())
    if n == 0 and k == 0:
        break
    num = list(map(int,input().split()))
    idx = 0
    parent = defaultdict(int)
    for i in range(1,n):
        parent[num[i]] = num[idx]
        if i < n-1 and num[i+1] - num[i] != 1:
            idx +=1
    cnt = 0
    if parent[parent[k]]:
        for i in num:
            if parent[parent[i]] == parent[parent[k]] and parent[i] != parent[k]:
                cnt += 1
    print(cnt)