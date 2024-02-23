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

    def stack_permutations(self):
        rst = ""
        n_nums = self.readline()
        stack = []
        top = 1
        for i in range(1, n_nums + 1):
            num = self.readline()
            while top <= num:
                stack.append(top)
                top += 1
                rst += "+\n"

            if stack[-1] == num:
                stack.pop()
                rst += "-\n"
            else:
                print("NO")
                return
        print(rst)


sol = Solution()
sol.stack_permutations()
