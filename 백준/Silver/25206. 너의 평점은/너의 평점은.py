import sys

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt():
    return input().strip().split(" ")


def spt_map_int():
    return list(map(int, input().strip().split(" ")))


def sol():
    과목평점 = {
        "A+": 4.5,
        "A0": 4.0,
        "B+": 3.5,
        "B0": 3.0,
        "C+": 2.5,
        "C0": 2.0,
        "D+": 1.5,
        "D0": 1.0,
        "F": 0.0,
    }

    점수합 = 0.0
    학점합 = 0.0
    
    for _ in range(20):
        _, 학점, 등급 = spt()

        if 등급 == "P":
            continue

        학점 = float(학점)
        평점 = 과목평점[등급]


        점수합 += 학점 * 평점
        학점합 += 학점

    print(점수합 / 학점합)


sol()
