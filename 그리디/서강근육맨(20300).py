import sys
input = sys.stdin.readline
n = int(input())
sonsil = list(map(int,input().split()))
sonsil.sort()

ans = []
if len(sonsil) % 2 != 0:

    ans.append(sonsil[-1])
    sonsil = sonsil[:-1]
    sonsil_original = sonsil[:len(sonsil)//2]
    sonsil_reverse = sonsil[len(sonsil)//2:]
    for i in range(len(sonsil_original)):
        ans.append(sonsil_original[i]+sonsil_reverse[len(sonsil_original)-1-i])
    print(max(ans))
else:
    sonsil_original = sonsil[:len(sonsil)//2]
    sonsil_reverse = sonsil[len(sonsil)//2:]
    for i in range(len(sonsil_original)):
        ans.append(sonsil_original[i]+sonsil_reverse[len(sonsil_original)-1-i])
    print(max(ans))
    
