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

    def employee(self):
        n = self.readline()
        for _ in range(n):
            p = self.readline()
            emp = []

            for _ in range(p):
                emp.append(self.readline())
            emp.sort(key=lambda x: x[0])

            rst = [emp[0]]
            right_min = emp[0][1]

            for i in range(1, len(emp)):
                if emp[i][1] <= right_min:
                    rst.append(emp[i])
                    right_min = emp[i][1]
            print(len(rst))


sol = Solution()
sol.employee()
