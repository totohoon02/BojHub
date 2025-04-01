def solution(word):
    answer = 0
    vowels = ["A", "E", "I", "O", "U"]
    idx = -1
    
    def dfs(s):
        nonlocal idx, answer

        if len(s) > 5:
            return

        idx += 1
        
        if s == word:
            answer = idx
            return
        
        for v in vowels:
            dfs(s + v)

    dfs("")
    return answer