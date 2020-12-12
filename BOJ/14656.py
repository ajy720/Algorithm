if __name__ == "__main__":
    n = int(input())

    arr = [*map(int, input().split())]

    ans = len([0 for idx, value in enumerate(arr) if idx+1 != value])
    
    print(ans)

