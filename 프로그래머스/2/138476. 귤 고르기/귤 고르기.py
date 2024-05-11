from collections import Counter

def solution(k, tangerine):
    answer = 0

    c = Counter(tangerine)
    count = 0
    
    commons = c.most_common()

    for _, num in commons:
        count += num
        answer += 1
        if count >= k:
            break
    
    return answer