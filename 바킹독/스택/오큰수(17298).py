n = int(input())
nums = list(map(int,input().split()))
NGE = [-1] * n
stack = [0]

for i in range(1,n):

    while stack and nums[stack[-1]] < nums[i]:
        NGE[stack.pop()] = nums[i]
    stack.append(i)
print(*NGE)