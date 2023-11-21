from itertools import permutations
k,m = map(int,input().split())
lst = []
MAX = 98765 // 10**(5-k)

check = [0] * (MAX+1)
prime_lst = set()
for i in range(2,MAX+1):
    if check[i] == 0:
        check[i] = 1
        prime_lst.add(i)
        j = 1
        while i * j <= MAX:
            check[i*j] = 1
            j += 1

for num in permutations(range(10),k):
    if num[0] == 0:
        continue
    N = int(''.join(list(map(str,num))))
    temp = N
    while temp % m == 0:
        temp //= m
    i = 2
    temp_lst = []
    while i <= int(temp**0.5):
        if temp % i == 0:
            if i in prime_lst and temp//i in prime_lst:
                j = 2
                while j < N // 2:
                    if j in prime_lst and N-j in prime_lst:
                        lst.append(N)
                        break
                    j += 1
            break
        i += 1
print(len(lst))