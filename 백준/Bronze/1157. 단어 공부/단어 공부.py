import sys

input = sys.stdin.readline

def spt():
    return input().split(" ")


def spt_map_int():
    return list(map(int, input().split(" ")))


def assertEqual(a, b):
    assert a == b


def sol():
    from collections import Counter
    c = Counter(list(input().strip().lower()))
    
    c2 = c.most_common(2)

    if len(c2) == 1:
        k, v = c2[0]
        print(k.upper())
    else:
      k1, v1 = c2[0]
      k2, v2 = c2[1]

      if v1 == v2:
          print("?")
      else:
          print(k1.upper())


sol()