m,n = map(int,input().split())

state = [0]*(n+1)
state[1] = 1

for i in range(2, int(n**0.5) + 1):
    if state[i] == 0:
        for j in range(i * i, n + 1, i):
            state[j] = 1
result = []
for i in range(m,n+1):
    if state[i] == 0:
        result.append(i)

for i in result:
    print(i)