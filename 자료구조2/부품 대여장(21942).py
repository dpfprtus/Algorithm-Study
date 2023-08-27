n,l,f = input().split()
print(n,l,f)
result = []
dic = {}
for _ in range(int(n)):
    a,b,c,d = input().split()  
    key = c+' '+d 
    if key not in dic:
        dic[key] = (a,b)
    else:
        day,time = dic[key]
        
        
        
        