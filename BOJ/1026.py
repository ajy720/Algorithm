if __name__ == "__main__":
    n = int(input())

    arr1 = sorted([*map(int, input().split())], reverse=True)
    arr2 = sorted([*map(int, input().split())])

    print(sum([arr1[i]*arr2[i] for i in range(n)]))