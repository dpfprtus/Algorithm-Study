import heapq

n = int(input())
num = [int(input()) for _ in range(n)]
heapq.heapify(num)
result = 0
if len(num) == 1:
    print(0)
    exit()
while num:
    first = heapq.heappop(num)
    second = heapq.heappop(num)
    tmp = first+second
    if num:
        heapq.heappush(num,tmp)
    result += tmp
print(result)