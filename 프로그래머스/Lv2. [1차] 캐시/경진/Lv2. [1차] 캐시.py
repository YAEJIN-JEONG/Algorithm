# https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque


def solution(cacheSize, cities):
    cache, answer = deque(), 0

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()

        # 캐시에 있으면 해당 도시 지움
        if city in cache:
            cache.remove(city)
            answer += 1
        # 캐시 가장 뒤에 있는 도시 지움
        elif len(cache) >= cacheSize:
            answer += 5
            cache.popleft()
        else:
            answer += 5

        # 캐시에 현재 도시 입력
        cache.append(city)

    return answer
