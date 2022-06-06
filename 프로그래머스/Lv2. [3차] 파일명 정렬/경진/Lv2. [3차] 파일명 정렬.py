# https://programmers.co.kr/learn/courses/30/lessons/17686
import re


def solution(files):
    # NUMBER 기준 정렬
    files.sort(key=lambda x: int(re.split('([0-9]+)', x)[1]))
    # HEAD 기준 정렬
    files.sort(key=lambda x: re.split('[0-9]+', x)[0].lower())
    return files
