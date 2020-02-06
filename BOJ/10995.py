n = int(input())
 
for i in range(n):
	str = "* "*n
	if i%2 == 1:
		str = " "+str.rstrip(" ")
	print(str)