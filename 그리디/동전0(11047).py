n,k = map(int,input().split())
price = [int(input()) for _ in range(n)]
price.sort(reverse=True)
result = 0
cnt = 0
for i in price:
    if i > k:
        continue
    ans = k // i
    k -= i * ans
    cnt += ans
    if k == 0:
        break
print(cnt)
