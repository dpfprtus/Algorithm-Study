n = int(input())
nums = list(map(int,input().split()))
op_input = list(map(int,input().split()))
# 덧셈,뺄셈,곱셈,나눗셈

operator = []
if op_input[0] != 0:
    cnt = op_input[0]
    while cnt > 0:
        operator.append("+")
        cnt -= 1
if op_input[1] != 0:
    cnt = op_input[1]
    while cnt > 0:
        operator.append("-")
        cnt -= 1
if op_input[2] != 0:
    cnt = op_input[2]
    while cnt > 0:
        operator.append("*")
        cnt -= 1
if op_input[3] != 0:
    cnt = op_input[3]
    while cnt > 0:
        operator.append("/")
        cnt -= 1

op_length = len(operator)
ops = [0]*op_length

def cal(tmp):
    
    result = nums[0]
    for i in range(n-1):
        if tmp[i] == "+":
            result += nums[i+1]
        elif tmp[i] == "-":
            result -= nums[i+1]
        elif tmp[i] == "*":
            result *= nums[i+1]
        elif tmp[i] == "/":   
            result /= nums[i+1]
            result = int(result)
 
    return result

max_result = -float("inf")
min_result = float("inf")

visited = [0]*op_length

def dfs(x):
    global max_result
    global min_result
    
    if x == op_length:
        tmp = []
        for i in ops:
            tmp.append(operator[i])

        result = cal(tmp)
        max_result = max(max_result,result)
        min_result = min(min_result,result)
        return
    
    for i in range(op_length):
        if visited[i] == 0:
            ops[x] = i
            visited[i] = 1
            dfs(x+1)
            visited[i] = 0
dfs(0)
print(max_result)
print(min_result)