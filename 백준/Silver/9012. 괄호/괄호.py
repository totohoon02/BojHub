T = int(input())
result = []
for _ in range(T):
    is_vps = True
    stack = []
    brackets = list(input())

    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack:
                is_vps = False
                break
            stack.pop()

    if stack or not is_vps:
        result.append("NO")
    else:
        result.append("YES")

for rst in result:
    print(rst)