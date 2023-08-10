from sys import stdin


num = int(input())

for i in range(0,num):

    result = []
    isVps = True
    vps = stdin.readline().rstrip()

    for j in vps:
  
        if(j == "("):
            result.append(j)
        if(j==")"):
            if result:
                result.pop() #()로 매칭되는거라 pop시킨다
            elif not result:
                isVps = False
                break
    if not result and isVps:
        print("YES")
    elif result or not isVps:
        print("NO")
    

    
      
