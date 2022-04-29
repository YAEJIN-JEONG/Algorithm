def Rev(num):

  li=reversed(list(str(num)))
  return int(''.join(li))

x,y = map(int,input().split())
print(Rev(Rev(x) + Rev(y)))
