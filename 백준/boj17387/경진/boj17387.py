# https://www.acmicpc.net/problem/17387
# 선분 교차 2
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))


# counter-clockwise
def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


# 교차 여부
def cross(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2

    d1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    d2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    if d1 == 0 and d2 == 0:
        return min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)
    else:
        return d1 <= 0 and d2 <= 0


print(1 if cross(line1, line2) else 0)
