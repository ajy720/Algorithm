if __name__ == "__main__":
    n = int(input())

    arr = [*map(int, input().split())]

    stack = [0]

    for i in range(1, n):
        while stack and arr[stack[-1]] < arr[i]:
            arr[stack[-1]] = arr[i]
            stack.pop(-1)

        stack.append(i)

    while stack:
        arr[stack[-1]] = -1
        stack.pop(-1)

    print(*arr)




