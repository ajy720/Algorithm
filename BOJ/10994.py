def solve(lt, rb):
    if lt == rb:
        arr[lt][rb] = '*'
        return

    else:
        arr[lt][lt:rb+1] = ['*'] * (rb-lt+1)
        arr[rb][lt:rb+1] = ['*'] * (rb-lt+1)
        for i in range(lt+1, rb):
          arr[i][lt] = arr[i][rb] = '*'

    solve(lt+2, rb-2)


if __name__ == "__main__":
    n = int(input())

    size = 4 * n - 3

    arr = [[' '] * size for _ in ' ' * size]

    solve(0, size-1)

    for i in arr:
      print(''.join(i))