s = input()

#전부 0으로 바꾸는 경우.
count_0 = 0
#전부 1로 바꾸는 경우.
count_1 = 0
if s[0] == '1':
    count_0 += 1
else:
    count_1 += 1
    
for x in range(len(s)-1):
    if s[x] != s[x+1]:
        if s[x+1] == '1':
            count_0 += 1
        else:
            count_1 += 1
print(min(count_0,count_1))