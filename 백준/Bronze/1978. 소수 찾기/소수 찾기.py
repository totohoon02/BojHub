def gen_prime(n):
    nums = [True] * (n+1)

    primes = set()

    for i in range(2, n):
        if nums[i]:
            primes.add(i)
            j = i
            while j < n:
                nums[j] = False
                j += i
    return primes


primes = gen_prime(1000)

n = int(input())
nums = list(map(int, input().split(" ")))

count = 0
for num in nums:
    if num in primes:
        count += 1

print(count)
