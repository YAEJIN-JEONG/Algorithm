t=int(input())
for i in range(t):
    n=int(input())
    li = [0] * 101
    li[0]=1
    li[1]=1
    li[2]=1
    li[3]=2
    li[4]=2
    for j in range(5,n+1):
        li[j]=li[j-5]+li[j-1]
    print(li[n-1])