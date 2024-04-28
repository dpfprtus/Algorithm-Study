import sys
input = sys.stdin.readline

while True:
    square = list(map(int,input().split()))
    stack = []
    max_area = 0
    if square[0] == 0:
        break
    for i in range(1,square[0]+1):
        if not stack:
            stack.append((i,square[i]))
        else:
            if stack[-1][1] <= square[i]:
                stack.append((i,square[i]))
            else:

                while stack and stack[-1][1] > square[i]:
                    remove = stack.pop()
                    if len(stack) == 0:
                        width = i-1
                    else:
                        width = i - stack[-1][0] - 1
                    max_area = max(max_area,width * remove[1])
                stack.append((i,square[i]))
    while stack:
        remove = stack.pop()
        if len(stack) == 0:
            width = square[0]
        else:
            width = (square[0] - stack[-1][0])
        max_area = max(max_area, width * remove[1])
    print(max_area)