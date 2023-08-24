from sys import stdin
from collections import defaultdict
result = defaultdict(int)
cnt = 0
while True:
    try:
        a = stdin.readline().rstrip()
        if not a:
            break
        result[a] += 1
        cnt+=1
    except:
        break
result =sorted(result.items())

for a,b in result:
    print("%s %.4f" % (a,round(b/cnt*100,4)))
#round(0.5),rount(-0.5)는 모두 0이다 따라서 f를 써야한다.