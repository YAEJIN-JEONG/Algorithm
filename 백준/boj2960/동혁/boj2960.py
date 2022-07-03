a,b = map(int, input().split(' '))
li =[i for i in range(2,a+1)]
count = 0

while True:
    i = li.pop(0)
    count+=1
    if b == count:
        print(i)
        break
    for j in li:
        if j%i==0:
            count+=1
            if b == count:
                print(j)
                break
            li.remove(j)
    if b == count:
        break