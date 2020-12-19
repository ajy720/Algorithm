if __name__ == "__main__":
    n = [*map(int, input())]

    if len(n) > 1:
        term = n[1] - n[0]

    for i in range(1, len(n)):
        if n[i] - n[i - 1] != term:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            exit()

    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
