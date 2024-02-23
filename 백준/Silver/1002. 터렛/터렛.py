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

    def turret(self):
        num_cases = self.readline()
        for _ in range(num_cases):
            x1, y1, r1, x2, y2, r2 = self.readline()
            num_poses = 0
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

            if x1 == x2 and y1 == y2:
                if r1 == r2:
                    num_poses = -1  # 상동
                else:
                    num_poses = 0  # 내부
            else:
                if d > r1 + r2:
                    num_poses = 0  # 접접 x
                elif d == r1 + r2:
                    num_poses = 1  # 외접
                elif abs(r1 - r2) == d:
                    num_poses = 1  # 내접
                elif abs(r1 - r2) < d < abs(r1 + r2):
                    num_poses = 2  # 두 점에서 만남
                else:
                    num_poses = 0  # 두점과 내부 사이
            print(num_poses)


sol = Solution()
sol.turret()
