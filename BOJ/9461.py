pi = [1, 1, 1, 2, 2]

for _ in range(int(input())):
    n = int(input())-1
    
    if n >= len(pi):
        for i in range(len(pi), n+1):
            pi.append(pi[i-1] + pi[i-5])

    print(pi[n])