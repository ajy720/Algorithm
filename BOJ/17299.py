if __name__ == "__main__":
    def F(a):
        global table
        return table[a]

    # NGF 스택 유지하며, NGF 반환
    def NGF(a):
        global stack
        while stack and F(a) >= F(stack[-1]):
            stack.pop()

        ret = stack[-1] if stack else -1
        stack.append(a)

        return ret
    
    
    n = int(input())
    arr = list(map(int, input().split()))

    table = dict()
    stack = []
    res = [-1] * n

    for x in arr:
        cnt = table.setdefault(x, 0)

        table.update({x: cnt + 1})

    # print(table)

    for idx in range(n - 1, -1, -1):
        x = arr[idx]

        # print(f"idx: {idx}, x: {x}, stack: {stack}")

        res[idx] = NGF(x)

    print(*res)
