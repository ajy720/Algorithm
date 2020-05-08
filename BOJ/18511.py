if __name__ == "__main__":
    
    n, k = input().split()
    s = sorted(map(int, input().split()), reverse=True)
    ans = 0
    
    if int(n[0]) in s:
        pass
    else:
        for i in s:
            if i <= int(n[0]):
                ans = i
                break
        for i in n[1:]:
            ans *= 10
            ans += s[0]
    
    print(ans)
        


'''
100000000 8
1 2 3 4 5 6 7 8

546 3
8 7 9

907 2
9 4

984054 3
4 5 6

657 3
1 5 7

657 3
6 7 8
'''