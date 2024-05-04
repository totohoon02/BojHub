def solution(n, words):
    w = set()
    
    count = 1
    num = 1
    
    prev = ""
    for word in words:
        if word in w or (prev != "" and prev[-1] != word[0]):
            return [num, count]
        else:
            w.add(word)
            prev = word
            num += 1
            if num > n:
                num = 1
                count += 1
                
    return [0, 0]
