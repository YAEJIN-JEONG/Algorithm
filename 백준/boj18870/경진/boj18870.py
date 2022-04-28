# https://www.acmicpc.net/problem/18870
# 좌표 압축
from sys import stdin

n = int(stdin.readline())
n_list = list(map(int, stdin.readline().split()))

# set 으로 중복제거, 오름차순 정렬 후 index 값이 압축된 좌표 값
compress = {elem: i for i, elem in enumerate(sorted(set(n_list)))}

print(' '.join(map(str, [compress[i] for i in n_list])))
