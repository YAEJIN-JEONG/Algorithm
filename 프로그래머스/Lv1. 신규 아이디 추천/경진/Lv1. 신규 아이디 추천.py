# https://programmers.co.kr/learn/courses/30/lessons/72410
import re


def solution(new_id):
    # 적혀있는 단계별로 진행
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\\-_.]', '', new_id)
    new_id = re.sub('[.]+', '.', new_id)
    new_id = new_id.lstrip('.').rstrip('.')
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    if len(new_id) <= 2:
        c = new_id[-1]
        while len(new_id) < 3:
            new_id += c

    return new_id
