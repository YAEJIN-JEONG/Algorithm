data=input()
result = int(data[0])

for i in range(1,len(data)):
    #두 번째 이후 값 고려
    num = int(data[i])
    #result가 0이나 1인 경우 고려
    if result == 0 or result == 1:
        result += num
    elif num == 0 or num == 1:
        result += num
    else:
        result *= num
print(result)
