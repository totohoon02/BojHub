import sys

input = sys.stdin.readline

def spt():
    return input().split(" ")


def spt_map_int():
    return list(map(int, input().split(" ")))


def assertEqual(a, b):
    assert a == b


def sol():
    n = int(input())
    l = 2 * n - 1 # 9
    
    for i in range(1, n + 1):
        star = "*" * (2 * i - 1)
        
        t = " " * ((l - len(star)) // 2) + star
        print(t)

    for i in range(n-1, 0, -1):
        star = "*" * (2 * i - 1)
        
        t = " " * ((l - len(star)) // 2) + star
        print(t)

sol()
