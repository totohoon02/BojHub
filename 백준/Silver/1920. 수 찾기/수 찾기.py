import sys

input = sys.stdin.readline


def spt():
    return list(map(int, input().split(" ")))


n = int(input())
y = spt()
_ = input()
x = spt()

y.sort()

for num in x:
    start = 0
    end = len(y) - 1
    state = False

    while start <= end:
        mid = (start + end) // 2
        if y[mid] > num:
            end = mid - 1
        elif y[mid] < num:
            start = mid + 1
        else:
            state = True
            break

    print(state * 1)
