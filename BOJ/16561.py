def combi(n:int , r:int)->int:
	if n == 0: return 0
	if n == 1: return 0
	if (n//2) < r: r = n-r
	
	res = 1
	for i in range(r):
		res *= (n-i)
		res //= (i+1)
	return res
	
print(combi(int(input())//3-1,2))