n = int(input())
rst = []
for _ in range(n):
    rst.append(input())

rst.sort(key=lambda x: int(x.split(" ")[0]))
for item in rst:
    print(item)