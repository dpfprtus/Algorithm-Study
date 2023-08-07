while True:
    try:
        first,second = input().split()
        result = ""
        count = 0
        for i in range(len(first)):
            for j in range(count,len(second)):
                if first[i:i+1] == second[j:j+1]:
                    result += second[j:j+1]
                    count = j+1
                    break

        if result == first:
            print("Yes")
        else:
            print("No")
    except EOFError:
        break
