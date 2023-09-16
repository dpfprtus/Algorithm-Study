import heapq
#너무 어렵다. 다음에 풀어보자
n = int(input())
visited = [False] * 100001
max_heap = []
min_heap = []

for _ in range(n):
    a,b,c = map(int,input().split())
    visited[a] = True
for i in range(int(input())):
    s = input().split()
    if s[0] == "recommend":
        if s[2] == "1":
            c = ""
            while not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            while c == s[1]:
                a,b,c = heapq.heappop(max_heap)
                if c != s[1]:
                    heapq.heappush(max_heap,(a,b,c))
            visited[b] = False
            print(b)
        else:
            
            
    elif s[0] == "recommend2":
        
    elif s[0] == "recommend3":
    elif s[0] == "add":
        heapq.heappush(max_heap,(-s[2],s[1],s[3]))
        heapq.heappush(min_heap,(s[2],s[1],s[3]))
        visited[s[1]] = True
    else:
        
        
        