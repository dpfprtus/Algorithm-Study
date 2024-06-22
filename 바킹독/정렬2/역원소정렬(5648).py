nums = list(map(int,input().split()))
length = nums[0]
nums = list(map(str,nums))
cnt = len(nums)-1
while cnt < length:
    tmp = list(map(str,input().split()))
    for i in tmp:
        cnt += 1
        nums.append(i)

for i in range(1,length+1):
    reverse = ''.join(reversed(nums[i]))
    tmp = ''
    flag = 0
    for j in reverse:
        if j == '0' and flag == 0:
            continue
        tmp += j
        flag = 1
    nums[i] = int(tmp)
nums = nums[1:]
nums.sort()
for i in nums:
    print(i)

    
