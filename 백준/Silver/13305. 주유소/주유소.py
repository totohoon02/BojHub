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

    def fuel(self):
        num_cities = self.readline()
        roads = self.readline()
        costs = self.readline()[:-1]

        min_cost = min(costs)

        ans = 0
        # 1. 최소 코스트인 도시가 아니면 다음 도시로 이동하기 위한 연료만 구매
        # 2. 최소 코스트일 경우 남은 거리를 모두 이동하기 위한 연료 구매
        # 3. 마지막 도시는 고려할 필요 x
        for i in range(num_cities - 1):
            if costs[i] != min_cost:
                ans += roads[i] * costs[i]
            else:
                ans += sum(roads[i:]) * costs[i]
                break

        print(ans)


sol = Solution()
sol.fuel()
