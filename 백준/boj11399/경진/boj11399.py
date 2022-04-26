# https://www.acmicpc.net/problem/11399
# ATM
from sys import stdin

n = int(stdin.readline())
# 뽑는 데 시간이 적게 걸리는 사람부터 뽑으면 됨
n_list = sorted(list(map(int, stdin.readline().split())))

# 시간 총 합
total = 0
# 지금 까지 걸린 시간 부분 합
sub_total = 0

for i in n_list:
    total += sub_total + i
    sub_total += i

print(total)
