def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        flag = True
        s = skill
        for t in tree:
            if t in s:
                if t != s[0]:
                    flag = False
                    break
                else:
                    s = s[1:]
        
        if flag:
            answer += 1

    return answer


if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    print(solution(skill, skill_trees))
    pass
