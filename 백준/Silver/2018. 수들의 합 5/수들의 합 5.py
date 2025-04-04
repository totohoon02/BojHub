import sys

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    n = iinput()
    
    start_index = 1
    end_index = 1
    count = 1
    sum = 1

    while end_index != n:
        if sum == n:
            count += 1

        if sum >= n:
            sum -= start_index
            start_index += 1
        elif sum < n:
            end_index += 1
            sum += end_index
        else:
            end_index += 1
            sum += end_index
    
    print(count)

sol()
