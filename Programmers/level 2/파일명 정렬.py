import sys

input = sys.stdin.readline


def solution(files):
    answer = []
    for i, file in enumerate(files):
        for j in range(len(file)):
            s = j
            if file[j] in "0123456789":
                break
        for j in range(j, len(file) + 1):
            e = j
            try:
                if not file[j] in "0123456789":
                    break
            except:
                pass

        files[i] = [file[:s], file[s:e], file[e:]]

    answer = sorted(files, key=lambda x: (x[0].lower(), int(x[1])))

    answer = ["".join(i) for i in answer]

    return answer


if __name__ == "__main__":
    arr = [input().strip() for i in range(int(input()))]
    print(solution(arr))
