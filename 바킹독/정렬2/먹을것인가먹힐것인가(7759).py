t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    nums_a = list(map(int,input().split()))
    nums_b = list(map(int,input().split()))
    
    nums_a.sort()
    nums_b.sort()
    result = 0
    start = 0
    for j in range(a):
        while True:
            if start == b or nums_a[j] <= nums_b[start]:
                result += start
                break
            else:
                start += 1
    print(result)