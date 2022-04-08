# https://www.acmicpc.net/problem/1620
from sys import stdin

n, m = map(int, stdin.readline().split())

# 포켓몬 이름이 주어졌을땐 리스트에서
# 포켓몬 번호가 주어졌을땐 딕셔너리에서
pokemon_list, pokemon_dict = [0], {}

for i in range(1, n + 1):
    pokemon = stdin.readline().rstrip()
    pokemon_list.append(pokemon)
    pokemon_dict[pokemon] = i

for _ in range(m):
    s = stdin.readline().rstrip()
    # s가 숫자인지에 따라 분기
    if s.isdecimal():
        print(pokemon_list[int(s)])
    else:
        print(pokemon_dict[s])
