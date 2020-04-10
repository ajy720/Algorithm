if __name__ == "__main__":
    ans = [0, 1, 2, 4]
    for i in range(4, 12):
        ans.append(sum(ans[-3:]))
    
    for _ in range(int(input())):
        print(ans[int(input())])