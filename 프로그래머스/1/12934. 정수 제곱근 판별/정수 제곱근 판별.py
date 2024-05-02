def solution(n):
    answer = (int(n ** 0.5) + 1) ** 2 if n ** 0.5 == n // (n ** 0.5) else -1
    return answer