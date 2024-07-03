n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()
rope = [0]*(n)
max_len = n
for i in range(n):
    rope[i] = nums[i] * max_len
    max_len -= 1

print(max(rope))
   
