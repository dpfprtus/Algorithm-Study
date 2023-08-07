n = int(input())
bupum = list(map(int,input().split()))
m = int(input())
order = list(map(int,input().split()))
bupum.sort()
def binary(array,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return "no"

for x in range(m):
    print(binary(bupum,order[x],0,n-1))
    