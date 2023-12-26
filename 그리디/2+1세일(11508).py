n = int(input())
item = [int(input()) for _ in range(n)]
item.sort(reverse=True)
result = []
a = []
for i in item:
    a.append(i)
    if len(a) == 3:
        result.append(a)
        a = []
ans = 0
if len(result) == 0:
    print(sum(item))
else:
    for i in result:
        ans += sum(i[0:2])
    print(ans+sum(a))
