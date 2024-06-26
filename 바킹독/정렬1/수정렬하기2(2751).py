import sys
sys.setrecursionlimit(10**7)

n = int(input())
nums = [int(input()) for _ in range(n)]

def merge(st,en):
    mid = int((st+en)/2)
    left_idx = st
    right_idx = mid
    tmp = [0]*n
    for i in range(st,en):
        if left_idx >= mid:
            tmp[i] = nums[right_idx]
            right_idx += 1
        elif right_idx >= en:
            tmp[i] = nums[left_idx]
            left_idx += 1
        elif nums[left_idx] <= nums[right_idx]:
            tmp[i] = nums[left_idx]
            left_idx += 1
        elif nums[left_idx] > nums[right_idx]:
            tmp[i] = nums[right_idx]
            right_idx += 1
    for i in range(st,en):
        nums[i] = tmp[i]
    
def merge_sort(st,en):

    if st+1 == en:
        return
    mid = int((st+en) / 2)
    merge_sort(st,mid)
    merge_sort(mid,en)
    merge(st,en)

merge_sort(0,n)
print(*nums)