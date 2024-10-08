from utils import *

n, m = input_as_num_list()
mins = []
for _ in range(n):
    mins.append(min(input_as_num_list()))

print(max(mins))
