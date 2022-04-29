#점화식 n = (n-2) + (n-1)
li = [0, 1]
for i in range(2, 91):
  li.append(li[i - 2] + li[i - 1])

print(li[int(input())])