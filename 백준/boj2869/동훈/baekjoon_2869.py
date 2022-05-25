#!/usr/bin/python3
import math
up , sleep , height = map(int, input().split())

day = (height - sleep) / (up - sleep)

print(math.ceil(day)) 
