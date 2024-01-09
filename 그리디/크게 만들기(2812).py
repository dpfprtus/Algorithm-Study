import sys
input = sys.stdin.readline
n,k = map(int,input().split())
nums = input().rstrip()

ans = []
cnt = 0

for num in nums:
    while ans and num > ans[-1] and k>0:
        ans.pop()
        k-=1
    ans.append(num)

if k>0:
    print(''.join(ans[:-k]))
else:
    print(''.join(ans))

