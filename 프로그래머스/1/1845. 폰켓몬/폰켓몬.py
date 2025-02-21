def solution(nums):
    max_choice = len(nums) // 2
    n_choice = 0
    choice = set()
    
    
    for num in nums:
        if num not in choice:
            choice.add(num)
            n_choice += 1
            
            if n_choice == max_choice:
                break
    
    return n_choice