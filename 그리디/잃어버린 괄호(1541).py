s = input()
minus_split = s.split("-")

for i in range(len(minus_split)):
    if "+" in minus_split[i]:
        plus_split = minus_split[i].split("+")
        ans = 0
        for j in plus_split:
            ans += int(j)
        minus_split[i] = ans
    else:
        minus_split[i] = int(minus_split[i])

if len(minus_split) == 1:
    print(minus_split[0])
else:
    result = minus_split[0]
    for i in range(1,len(minus_split)):
        result -= minus_split[i]
    print(result)