def solution(food):
    f = ""
    for i in range(1, len(food)):
        f += str(i) * (food[i] // 2)
    answer = f + "0" + f[::-1]
    return answer