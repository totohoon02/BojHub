class Statistics:
    def __init__(self, n):
        self.n = n
        self.nums = [int(input()) for _ in range(n)]
        self.nums.sort()

    def run(self):
        print(self.average())
        print(self.center())
        print(self.most_common())
        print(self.xrange())

    def average(self):
        return int(round(sum(self.nums) / len(self.nums), 0))

    def center(self):
        return self.nums[int(len(self.nums) / 2)]

    def most_common(self):
        if len(self.nums) == 1:
            return self.nums[0]
        from collections import Counter
        c = Counter(self.nums)
        com = c.most_common(2)
        if com[0][1] == com[1][1]:
            return com[1][0]
        else:
            return com[0][0]

    def xrange(self):
        return self.nums[-1] - self.nums[0]


sol = Statistics(int(input()))
sol.run()
