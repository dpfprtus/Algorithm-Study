key = input()
secret = input()
data = []
result = ""
length = len(secret)
count = length // len(key)
key2 = sorted(key)
for k in range(0,length,count):
    result = secret[k:k+count]
    data.append((result)) 
    result = ""
data2 =[]
for i in range(len(key2)):
    data2.append((key2[i],data[i]))
print(data2)
result2 =""
for i in range(length):
    for k in range(len(key)):
        result = data2[k][1]
        result2 = result[i]
print(result2)