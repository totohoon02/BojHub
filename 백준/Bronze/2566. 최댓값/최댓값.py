import sys

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    coord = "11"
    max_value = 0

    for i in range(9):
        values = spt_map_int()
        cur_max = max(values)

        if cur_max > max_value:
            coord = str(i + 1) + str(values.index(cur_max) + 1)
            max_value = cur_max

    print(max_value)
    print(coord[0] + " " + coord[1])


sol()
