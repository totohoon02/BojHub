import math

def readline(as_int=True):
    import sys
    input = sys.stdin.readline
    line = input().split(" ")
    if len(line) == 1:
        return int(line[0])
    if as_int:
        return list(map(int, line))
    else:
        return line


T = readline()
for _ in range(T):
    x, y = readline()
    distance = y - x

    count = 0
    nearSqrt = math.floor(distance ** 0.5)
    nearSq = nearSqrt ** 2

    if distance <= 3:
        count = distance
    elif distance == nearSq:
        count = nearSqrt * 2 - 1
    elif nearSq < distance <= nearSq + nearSqrt:
        count = nearSqrt * 2
    elif nearSqrt + nearSq < distance:
        count = nearSqrt * 2 + 1
    print(count)
