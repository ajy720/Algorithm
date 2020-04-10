if __name__ == "__main__":
    n = 1000 - int(input())
    arr = [500, 100, 50, 10, 5, 1]
    ans = 0

    for i in arr:
        ans += n // i
        n %= i
    
    print(ans)