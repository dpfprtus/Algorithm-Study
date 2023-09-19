import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().rstrip()
    left = []
    right = []
    for i in s:
        if i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    right.reverse()
    left.extend(right)
    print(''.join(left))