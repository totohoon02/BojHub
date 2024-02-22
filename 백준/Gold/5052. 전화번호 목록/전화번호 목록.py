class PhoneBook:
    def __init__(self, n):
        self.n = n

    def is_consistent(self):
        n_num = int(input())
        nums = [input() for _ in range(n_num)]
        set_nums = set(nums)

        for num in nums:
            temp_num = num[:-1]
            while temp_num:
                if temp_num in set_nums:
                    print("NO")
                    return
                temp_num = temp_num[:-1]

        print("YES")


sol = PhoneBook(int(input()))
for _ in range(sol.n):
    sol.is_consistent()
