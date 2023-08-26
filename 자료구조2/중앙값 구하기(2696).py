t = int(input())

for _ in range(t):
    num_length = int(input())
    num = []
    for _ in range(num_length//10 + 1):
        num += list(map(int,input().split()))
    result = []
    for i in range(0,num_length,2):
        new_num = num[:i+1]
        new_num.sort()
        if len(new_num) == 1:
            result.append(new_num[0])
            continue
        if len(new_num) % 2 == 0:
            print("new_num",new_num)
            result.append((new_num[len(new_num)//2-1]+new_num[len(new_num)+1])/2)
        else:
            result.append(new_num[len(new_num)//2])
    print(len(result))
    print(' '.join(map(str,result)))