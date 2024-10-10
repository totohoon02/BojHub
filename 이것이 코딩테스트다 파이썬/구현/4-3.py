from utils import *

# 8x8
# move 수평2수직1 수직2수평1
# 위치가 주어졌을 때 이동할 수 있는 좌표 수

p = input()  # a1
x, y = [ord(p[0]) - ord('a'), int(p[1]) - 1]
count = 0

# l r u d
moves = [[-2, 1], [-2, -1], [2, 1], [2, -1]]

# horizontal_first
for move in moves:
    if 0 < x + move[0] and x + move[0] < 8:
        if 0 < y + move[1] and y + move[1] < 8:
            count += 1

# vertiacl_first
for move in moves:
    if 0 < y + move[0] and y + move[0] < 8:
        if 0 < x + move[1] and x + move[1] < 8:
            count += 1

print(count)
