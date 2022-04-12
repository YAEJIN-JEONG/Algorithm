# https://www.acmicpc.net/problem/1764
from sys import stdin

n, m = map(int, stdin.readline().split())

# 듣도 못한 사람, 보도 못한 사람
set_1, set_2 = set(), set()

for _ in range(n):
    set_1.add(stdin.readline().rstrip())
for _ in range(m):
    set_2.add(stdin.readline().rstrip())

# 교집합
name_list = list(set_1 & set_2)
name_list.sort()

# 출력
print(len(name_list))
print('\n'.join(name_list))
