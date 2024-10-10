from utils import *

# NxN의 맵, (1,1)에서 시작
# L R U D 벽일 경우 무시
# 최종 위치 출력 프로그램

start = [1, 1]
n = int(input())
moves = input_as_str_list()


def is_out_bouded(m: list):
    if n < start[0] + m[0] or n < start[1] + m[1]:
        return True

    if 1 > start[0] + m[0] or 1 > start[1] + m[1]:
        return True
    return False


for move in moves:
    if move == "L":
        if not is_out_bouded([-1, 0]):
            start[0] += -1

    if move == "R":
        if not is_out_bouded([1, 0]):
            start[0] += 1

    if move == "U":
        if not is_out_bouded([0, -1]):
            start[1] += -1

    if move == "D":
        if not is_out_bouded([0, 1]):
            start[1] += 1

# 좌표계 확인..
print(start[::-1])
