def solution(n):
    answer = 0
    start_num = 1
    while start_num <= n:
        temp = 0
        for i in range(start_num, n+1):
            temp += i
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
        start_num += 1
    return answer