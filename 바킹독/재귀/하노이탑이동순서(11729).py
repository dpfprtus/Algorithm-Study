n = int(input())


def func(a,b,c):
    if c == 1:
        print(a,b)
        return
    func(a,6-a-b,c-1)
    print(a,b)
    func(6-a-b,b,c-1)

cnt = 0
print(2**n-1)
func(1,3,n)