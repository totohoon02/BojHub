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

    def sensor(self):
        # n : 센서의 개수, k : 집중국의 개수
        n = self.readline()
        k = self.readline()

        if k >= n:
            print(0)
            return
            
        # n개 센서들의 좌표
        coordinates = self.readline()
        coordinates.sort()

        distances = [coordinates[i + 1] - coordinates[i] for i in range(len(coordinates) - 1)]
        distances.sort()

        print(sum(distances[:n - k]))


sol = Solution()
sol.sensor()
