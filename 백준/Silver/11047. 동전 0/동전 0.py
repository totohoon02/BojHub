class Solution:
    def readline(self, as_int=True):
        import sys
        input = sys.stdin.readline
        line = input().split(" ")
        if len(line) == 1:
            return int(line[0])
        if as_int:
            return list(map(int, line))
        else:
            return line

    def coin_0(self):
        from collections import deque
        n, k = self.readline()
        coins = deque()
        for _ in range(n):
            coins.appendleft(self.readline())

        count = 0
        amount = k
        for coin in coins:
            while amount >= coin:
                amount -= coin
                count += 1

        print(count)

sol = Solution()
sol.coin_0()
