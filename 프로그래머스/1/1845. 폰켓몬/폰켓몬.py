def solution(nums):
	# 최대 가져갈 수 있는 폰켓몬 수
	max_choice = len(nums) // 2
	s = set(nums)
	return min(max_choice, len(s))