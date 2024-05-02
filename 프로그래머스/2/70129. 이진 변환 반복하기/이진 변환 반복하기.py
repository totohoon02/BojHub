def solution(s):
    answer = [0, 0]
    while s != "1":
        temp = s.replace("0", "")
        answer[0] += 1
        answer[1] += (len(s) - len(temp))
        
        s = bin(len(temp))[2:]
        
    return answer