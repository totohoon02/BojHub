# 가로 >= 세로
# ㅁㅁㅁ
# ㅁㅁㅁ
# 노랑 가로가 더 긴 경우의 수 (6, 1), (3, 2)
# 갈색 : 양쪽 세로 길이 * 2 + 가로길이 * 2 + 4
def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    
    for h in range(1, yellow):
        w = yellow / h
        if w < h:
            break
        
        br = h * 2 + w * 2 + 4
        
        if br == brown:
            return [w + 2, h + 2]
