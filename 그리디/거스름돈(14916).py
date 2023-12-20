coin = int(input())
residual = 0
result = 0

while True:
    if coin % 5 == 0:
        result += coin // 5
        coin %= 5
        break
    else:
        coin -= 2
        result += 1
    if coin <= 0:
        break
if coin == 0:
    print(result)
else:
    print(-1)
    
