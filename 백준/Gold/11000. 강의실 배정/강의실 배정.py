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

    def classroom(self):
        import heapq

        n = self.readline()
        lectures = []
        for _ in range(n):
            lectures.append(self.readline())
        lectures.sort(key=lambda x: (x[0]))

        rooms = [lectures[0][1]]
        heapq.heapify(rooms)

        for i in range(1, len(lectures)):
            start, end = lectures[i]

            min_end = heapq.heappop(rooms)
            heapq.heappush(rooms, end)
            if start < min_end:
                heapq.heappush(rooms, min_end)

        print(len(rooms))


sol = Solution()
sol.classroom()
