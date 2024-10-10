# 00:00:00부터 n시 59분 59초까지 3이 하나라도 포함 카운트

n = int(input())
h, m, s = 0, 0, 0
count = 0

while h != n or m != 59 or s != 59:
    s += 1
    if s == 60:
        m += 1
        s = 0

    if m == 60:
        h += 1
        m = 0

    if '3' in str(s):
        count += 1
        continue

    if '3' in str(m):
        count += 1
        continue

    if '3' in str(h):
        count += 1

print(count)
