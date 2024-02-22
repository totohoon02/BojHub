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

    def maxHeap(self):
        import heapq
        heap = []
        n = self.readline()
        for _ in range(n):
            num = self.readline()
            if num != 0:
                heapq.heappush(heap, num)
            else:
                if not heap:
                    print(0)
                    continue
                pop_num = heapq.heappop(heap)
                print(pop_num)


sol = Solution()
sol.maxHeap()
