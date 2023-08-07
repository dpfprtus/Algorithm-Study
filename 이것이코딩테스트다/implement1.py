n = int(input())

count = 0
for x in range(n+1):
    for j in range(60):
        for i in range(60):
            if "3" in str(x) or "3" in str(j) or "3" in str(i):
                count += 1
print(count)
