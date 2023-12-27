n = int(input())
length = list(map(int,input().split()))
price = list(map(int,input().split()))
result = 0
min_price = price[0]
for i in range(len(length)):
    if min_price > price[i]:
        min_price = price[i]
    result += length[i] * min_price
print(result)
    
    