def solution(brown, yellow):
    nums, col = brown + yellow, (brown + yellow) // 3
    while True:
        if col * (nums // col) == nums and (col + nums // col) * 2 - 4 == brown: return [col, nums // col] 
        col -= 1
