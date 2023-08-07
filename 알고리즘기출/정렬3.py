import heapq

n = int(input())
data = [int(input()) for _ in range(n)]
heapq.heapify(data)
result = 0
while len(data) != 1:
    one = heapq.heappop(data)
    two = heapq.heappop(data)
    sum = one + two
    result += sum
    heapq.heappush(data,sum)
print(result)