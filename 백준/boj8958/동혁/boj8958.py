n = int(input())
point = 0
for i in range(n):
    words = list(map(str,input().split('X')))
    for j in words:
        point += len(j) * (len(j)+1) / 2
    print(int(point))
    point = 0