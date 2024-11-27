n = int(input())

for _ in range(n):
    strs = input()
    total_score = 0
    cur_score = 0
    for c in strs:
        if c == "O":
            cur_score += 1
            total_score += cur_score
        else:
            cur_score = 0

    print(total_score)
