s = input()
cnt = 0
result = ""
for i in range(len(s)):
    if s[i] == "X":
        cnt += 1
    if cnt == 2 and (i == len(s)-1 or s[i+1] != "X" ):
        result += "BB"
        cnt = 0
        continue
    if cnt == 4:
        result += "AAAA"
        cnt = 0
        continue
    if s[i] == ".":
        result += "."
    if cnt % 2 != 0 and (i == len(s)-1 or s[i+1] =="."):
        result = "-1"
        break 

print(result)