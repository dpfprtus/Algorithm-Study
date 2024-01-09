import heapq

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)
result = 0
while len(card)>1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    result += a+b
    heapq.heappush(card,a+b)
print(result)