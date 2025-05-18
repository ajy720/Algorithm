INSERT = "insert"
DEPART = "depart"
RELOCATE = "relocate"

if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = input().split()

    for _ in range(m):
        cmd = input().split()
        cmd, target = cmd[0], cmd[1:]

        if cmd == INSERT:
            arr.insert(int(target[1]), target[0])

        elif cmd == DEPART:
            arr.remove(target[0])

        elif cmd == RELOCATE:
            target, bias = target[0], int(target[1])
            pos = arr.index(target) + bias
            arr.remove(target)
            arr.insert(pos, target)

    print(*arr, sep=" ")
