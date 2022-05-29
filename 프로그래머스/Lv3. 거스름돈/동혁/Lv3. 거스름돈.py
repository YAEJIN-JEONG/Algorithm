def solution(n, money):
    # 메모이제이션
    memo = [0] * (n + 1)
    memo[0] = 1

    # 주어진 동전에 하나씩 접근
    for coin in money:
        for price in range(coin, n + 1):
            memo[price] += memo[price - coin]

    return  memo[n] % 10000000007
