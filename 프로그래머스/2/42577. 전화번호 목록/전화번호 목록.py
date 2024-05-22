def solution(phone_book):
    ps = set(phone_book)
    
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in ps:
                return False
    return True