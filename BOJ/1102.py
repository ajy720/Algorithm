if __name__ == "__main__":
    arr = [input() for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8):
            if abs(i - j) % 2 == 0 and arr[i][j] == "F":
                cnt += 1

    print(cnt)
