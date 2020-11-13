import sys

input = sys.stdin.readline

if __name__ == "__main__":
    k, n = map(int, input().split())

    arr = sorted([int(input()) for _ in range(k)])

    arr = [str(i) for i in arr] + [str(arr[-1])] * (n-k)
    
    arr.sort(reverse=True)

    out = [[] for _ in range(10)]

    for i in range(len(arr)):
        out[int(arr[i][0])].append(arr[i])

    for idx, t in enumerate(out):
        # 여기서 각 자리수에 대한 최적해를 구해야 함
        for i in range(len(t)):
            for j in range(1, len(t)):
                if int(t[j] + t[j-1]) > int(t[j-1] + t[j]):
                    t[j], t[j-1] = t[j-1], t[j]

        out[idx] = ''.join(t)

    out.reverse()

    print(''.join(out))