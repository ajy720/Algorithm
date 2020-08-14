import math
import sys

input = sys.stdin.readline
prime = []

def getPrime(n):
	global prime
	prime = [False, False] + [True] * (n-1)
	ret = []

	for i in range(2, int(math.sqrt(n)) + 1):
		if prime[i]:
			ret.append(i)
			for j in range(i * 2, n + 1, i):
				prime[j] = False
		else:
			continue
	
	return ret


if __name__ == "__main__":
	arr = []
	while 1:
		arr.append(int(input()))

		if arr[-1] == 0:
			arr.pop(-1)
			break

	primeN = getPrime(max(arr))

	for value in arr:
		flag = False
		for i in primeN:
			if i > value:
				break

			if prime[value-i]:
				print(f'{value} = {i} + {value-i}')
				flag = True
				break

		if not flag:
			print("Goldbach's conjecture is wrong.")
