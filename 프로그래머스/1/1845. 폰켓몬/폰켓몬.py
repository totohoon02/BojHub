def solution(nums):
    max_kind = len(nums) // 2
    kind = set()
    
    for num in nums:
        kind.add(num)
        if(len(kind) == max_kind):
            break
    return len(kind)