import sys

input = sys.stdin.readline


def calc(n, arr):  # O(n^2)
    dp = [set() for _ in range(n)]

    for i in range(n):
        # case 1 : i - j ~ i + j�� �Ӹ������ ���(Ȧ���� ����)
        s, e = i, i
        while s >= 0 and e < n:
            if arr[s] == arr[e]:
                dp[s].add(e)  # ���� �� �������� ȸ�� ¦ ����

            else:
                break

            s -= 1
            e += 1

        # case 2 : i - j ~ i + j + 1 �� �Ӹ������ ���(¦���� ����)
        s, e = i, i + 1
        while s >= 0 and e < n:
            if arr[s] == arr[e]:
                dp[s].add(e)  # ���� �� �������� ȸ�� ¦ ����

            else:
                break

            s -= 1
            e += 1

    return dp


if __name__ == "__main__":
    global arr, ans

    n = int(input().strip())
    arr = [*map(int, input().split())]
    ans = calc(n, arr)

    for _ in range(int(input())):  # O(m)
        s, e = map(int, input().split())

        if e - 1 in ans[s - 1]:  # O(1)
            print(1)
        else:
            print(0)
