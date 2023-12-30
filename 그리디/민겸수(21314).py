s = input()
result = ""
ans = 1
for i in range(len(s)):
    if s[i] == 'M':
        ans *= 10
        if i == len(s)-1:
            result += str("1"*(str(ans).count("0")))
    elif s[i] == 'K':
        if ans > 2:
            result += str(ans*5)
            ans = 1
        else:
            if ans == 2:
                result += "1"
                ans = 1
            result += str(5)
            
print(result)
result = ""
ans = 0
for j in range(len(s)):
    if s[j] == 'M':
        ans += 1
        if j == len(s)-1:
            result += str(10 ** (ans-1)) 
    else:
        if ans > 0:
            result += str(10 ** (ans-1))  
        result += "5"
        ans =0
print(result)

