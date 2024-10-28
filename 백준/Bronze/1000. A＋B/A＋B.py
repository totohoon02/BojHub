import sys
input_data = sys.stdin.readline().rstrip()

nums = list(map(int, input_data.split(" ")))
print(sum(nums))