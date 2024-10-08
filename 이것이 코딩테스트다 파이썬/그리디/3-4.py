from utils import *

n, k = input_as_num_list()

count = 0
while n != 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1


print(count)
