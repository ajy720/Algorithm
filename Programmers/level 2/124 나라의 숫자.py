def solution(n):
    base124 = ['4', '1', '2']
    arr = []
    answer = []

    while n:
        arr.append(n % 3)
        answer.append(n % 3)
        n //= 3

    for i in range(len(arr)-1):
        if arr[i] == 0 or answer[i] == 0:
            answer[i+1] = (answer[i+1] + 2) % 3

    answer.reverse()

    if answer[0] == 0:
        answer.remove(0)

    return ''.join([base124[i] for i in answer])


if __name__ == "__main__":
    for n in range(1, 21):
        print(n, solution(n))
