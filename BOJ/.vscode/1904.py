n = int(input())
pi = [1, 1]

for i in range(2, n+1):
    pi.append((pi[i-1] + pi[i-2])%15746)

print(pi[n])