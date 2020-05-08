arr = [input() for _ in range(8)]
print(sum([arr[i][i % 2 :: 2].count("F") for i in range(8)]))
