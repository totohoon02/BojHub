def solution(price, money, count):
    total = sum([(i+1) * price for i in range(count)])
    if total <= money:
        return 0
    return total - money