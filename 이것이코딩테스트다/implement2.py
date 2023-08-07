place = input()
row = int(int(ord(place[0])) - int(ord('a'))) + 1
col = int(place[1])

steps = [[-2,-1],[-2,1],[2,1],[2,-1],[1,-2],[1,2],[-1,2],[-1,-2]]
count = 0
 
for step in steps:
    nextcol = col + step[0]
    nextrow = row + step[1]
    if (nextcol < 1 or nextcol > 8) or (nextrow < 1 or nextrow >8):
        continue
    else:
        count += 1

print(count)