ans = [0]*6
isTrue = [0]*14

def func(a,cur):

    if a == 6:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(cur,k):
        ans[a] = s[i]
        func(a+1,i+1)
       

while(True):
    inputs = list(map(int,input().split()))
    k = inputs[0]
    if k == 0:
        break
    s = inputs[1:]
    s.sort()
    func(0,0)
    #k개 원소를 가진 s에서 6개 수를 고른다.
    
    