from functools import cmp_to_key

def solution(numbers):
    return str(int(''.join(sorted([str(num) for num in numbers], key=cmp_to_key(comperator)))))

def comperator(a, b): return int(b+a) - int(a+b)