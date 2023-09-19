import sys
from collections import defaultdict
input = sys.stdin.readline
tree = defaultdict(int)
cnt = 0
while True:
    try:
        s = input().rstrip()
        if not s:
            break
        tree[s] +=1 
        cnt += 1

    except:
        break
tree = sorted(tree.items())
for a,b in tree:
    print("%s %.4f" % (a,round(b/cnt*100,4)))

