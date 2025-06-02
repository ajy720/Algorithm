if __name__ == "__main__":
    n = int(input())

    maxW, minW = -10000, 10000
    maxH, minH = -10000, 10000

    for _ in range(n):
        h, w = map(int, input().split())

        maxH = max(maxH, h)
        minH = min(minH, h)

        maxW = max(maxW, w)
        minW = min(minW, w)
        
    print((maxH - minH) * (maxW - minW))
