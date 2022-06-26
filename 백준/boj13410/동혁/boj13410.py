a,b=map(int,input().split(" "))
li=[]

for i in range(1,b+1):
    temp="".join(reversed(str(i*a)))
    li.append(int(temp))
li.sort(reverse=True)

print(li[0])