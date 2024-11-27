n = int(input())

for _ in range(n):
    strs = list(map(int, input().split(" ")))
    avg = sum(strs[1:]) / strs[0]

    count = 0
    for score in strs[1:]:
        if score > avg:
            count += 1

    print(f"{round(count / strs[0] * 100, 3)}%")