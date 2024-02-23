class Solution:
    def __init__(self):
        pass

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

    def meetings(self):
        n = self.readline()
        m = []
        for _ in range(n):
            start, end = self.readline()
            m.append((start, end))

        m.sort(key=lambda x: (x[1], x[0]))

        ans = 0
        now = 0
        for start, end in m:
            if now <= start:
                now = end
                ans += 1
        print(ans)
sol = Solution()
sol.meetings()
