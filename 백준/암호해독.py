secret = input()
n = int(input())
data = [input() for _ in range(n)]
change =""
case ="A"
for i in range(26):
    for k in range(len(secret)):
        change += chr((ord(secret[k])+i-97)%26 +97)
    for j in range(len(data)):
        if data[j] in change:
            case = data[j]
            break
    if case in change:
        print(change)
        break
    change = ""
        
