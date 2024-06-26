n = int(input())
nums = [int(input()) for _ in range(n)]
count = [0]*(max(nums)+1)

for i in nums:
    a = abs(i)
    count[a] += 1

for i in range(len(count)-1):
    count[i] = count[i] + count[i+1]

result = [0]*len(nums)
for num in nums:
    idx = count[num]
    result[idx-1] = num
    count[num] -= 1

for i in result:
    print(i)

    