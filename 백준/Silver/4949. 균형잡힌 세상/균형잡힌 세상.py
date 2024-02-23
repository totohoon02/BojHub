import sys

input = sys.stdin.readline


class Solution:
    def balanced_world(self):
        import re
        while True:
            line = input().rstrip()
            if line == ".":
                break
            line = re.sub(r"[\w\s.]", "", line)
            print(self.check_brackets(line))

    def check_brackets(self, brackets: str) -> str:
        is_vps = True
        stack = []
        for bracket in brackets:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            else:
                if not stack:
                    is_vps = False
                    break

                bk = stack.pop()
                if bk == "(" and bracket != ")":
                    is_vps = False
                    break
                elif bk == "[" and bracket != "]":
                    is_vps = False
                    break
                elif bk == "{" and bracket != "}":
                    is_vps = False
                    break

        if stack or not is_vps:
            return "no"
        return "yes"


sol = Solution()
sol.balanced_world()
