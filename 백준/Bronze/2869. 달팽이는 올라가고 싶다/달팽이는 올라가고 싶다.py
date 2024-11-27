import math

a, b, v = list(map(int, input().split(" ")))

count = math.ceil((v-a) / (a - b)) + 1
print(count)
