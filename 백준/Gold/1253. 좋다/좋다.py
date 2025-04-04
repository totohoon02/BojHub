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
    numbers = spt_map_int()
    numbers.sort()
    count = 0

    for i in range(n):
        target = numbers[i]
        start = 0
        end = n - 1

        while start < end:
            sum = numbers[start] + numbers[end]
            
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                if start != i and end != i:
                    count += 1
                    break
                elif start == i:
                    start += 1
                elif end == i:
                    end -= 1

    
    print(count)

sol()