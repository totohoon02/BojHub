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

    def atm(self):
        n_people = self.readline()
        times = self.readline()

        if type(times) is int:
            print(times)
            return

        times.sort()

        ans = 0
        for i in range(0, n_people):
            ans += times[i] * (n_people - i)

        print(ans)


sol = Solution()
sol.atm()
