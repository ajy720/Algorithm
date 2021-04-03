if __name__ == "__main__":
    arr = [*map(int, input().split())]
    time = int(input())
    time += arr[0] * 3600 + arr[1] * 60 + arr[2]

    print(time//3600 % 24,
          time % 3600//60,
          time % 60)
