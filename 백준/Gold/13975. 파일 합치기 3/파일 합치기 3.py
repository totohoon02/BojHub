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

    def merge_file(self):
        import heapq

        num_cases = self.readline()
        for _ in range(num_cases):
            num_chapter = self.readline()
            files = self.readline()
            heapq.heapify(files)
            cost = 0

            for _ in range(num_chapter - 1):
                a = heapq.heappop(files)
                b = heapq.heappop(files)
                cost += a + b
                heapq.heappush(files, a + b)
            print(cost)


sol = Solution()
sol.merge_file()
