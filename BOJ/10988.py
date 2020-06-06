def is_palindrom(arr, s, e):
    while s <= e:
        if arr[s] != arr[e]:
            return 0
        s +=1
        e -=1

    return 1

if __name__ == "__main__":
    s = input()

    print(is_palindrom(s, 0, len(s)-1))