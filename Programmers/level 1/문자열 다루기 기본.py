def solution(s):
    try: 
        int(s)
    except:
        return False

    return len(s) == 4 or len(s) == 6

if __name__ == "__main__":
    print(solution("a234"))
    print(solution("1234"))