# n을 거슬러 주기 위한 동전의 최소 갯수
n = 1260
count = 0
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)
