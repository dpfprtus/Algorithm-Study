from sys import stdin

test = int(input())

for _ in range(test):
    a = stdin.readline().rstrip()
    l_stack = []
    r_stack = []
    for i in a:
        if i == "-":
            if l_stack:
                l_stack.pop()
        elif i == "<":
            if l_stack:
                r_stack.append(l_stack.pop())
        elif i == ">":
            if r_stack:
                l_stack.append(r_stack.pop())
        else:
            l_stack.append(i)
    l_stack.extend(reversed(r_stack))
    print(''.join(l_stack))