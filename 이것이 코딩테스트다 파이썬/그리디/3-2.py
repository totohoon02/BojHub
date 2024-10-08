from utils import *

# n개 숫자, m번 합산, k번까지 반복
n, m, k = input_as_num_list()
# 입력 숫자들
nums = input_as_num_list()
nums.sort()

first = nums[-1]
second = nums[-2]
result = 0

while True:
    result += first
    k -= 1
    m -= 1

    if m == 0:
        break

    if k == 0:
        k = 3
        result += second
        m -= 1

        if m == 0:
            break


print(result)
