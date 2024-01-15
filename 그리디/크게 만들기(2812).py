import sys
input = sys.stdin.readline

n,k = map(int,input().split())
s = input().rstrip()
stack = []
for i in s:
    while stack and stack[-1] < int(i) and k != 0:
        stack.pop()
        k -= 1
    stack.append(int(i))
if k > 0:
    stack = stack[:-k]
print(''.join(map(str,stack)))