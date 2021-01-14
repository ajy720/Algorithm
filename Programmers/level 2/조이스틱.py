def solution(name):
    answer = 0

    for i in name:
        up = ord(i) - 65
        down = 26 - up

        answer += min(up, down)

    cursor = 0

    while cursor < len(name) - 1:

        if name[cursor] == 'A':
            t = cursor

            while t < len(name) and name[t] == 'A':
                t += 1

            if t == len(name):
                break
            
            if cursor != 0:
                answer -= 1
                cursor -= 1


            right = (len(name) - 1) - cursor
            left = (len(name) - 1) - t + cursor + 1

            if right > left:
                answer += left
                break

            else:
                answer += t - cursor
                cursor = t

        else:
            cursor += 1
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution("JEROEN"))
    print(solution("JAN"))
    print(solution("ABAAAAAAAAABB"))
    print(solution("AAAA"))
