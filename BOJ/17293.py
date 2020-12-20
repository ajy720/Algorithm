def bottle(k):
    if k > 1:
        return f"{k} bottles"
    elif k == 1:
        return f"{k} bottle"
    elif k == 0:
        return "no more bottles"
    elif k < 0:
        return f"{n} bottles"


if __name__ == "__main__":
    n = int(input())

    for i in range(n, 0, -1):
        print(f"{bottle(i)} of beer on the wall, {bottle(i)} of beer.")
        print(f"Take one down and pass it around, {bottle(i-1)} of beer on the wall.")
        print()

    print(f"No more bottles of beer on the wall, no more bottles of beer.")
    print(f"Go to the store and buy some more, {bottle(n)} of beer on the wall.")
