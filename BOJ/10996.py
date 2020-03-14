n = int(input())
for i in range(n*2):
    flag = True if i % 2 == 0 else False

    for i in range(n):
        print("*" if flag else " ", end="")
        flag ^= True    
    
    print()