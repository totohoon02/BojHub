def solution(s):
    arr = [s[0].upper()]
    prev = s[0]
    for i in range(1, len(s)):
        if s[i].isalpha() and prev == " ":
            arr.append(s[i].upper())
        elif s[i].isalpha():
            arr.append(s[i].lower())
        else:
            arr.append(s[i])
        prev = s[i]
    return "".join(arr)