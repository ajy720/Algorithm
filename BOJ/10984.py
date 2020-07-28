for _ in ' '*int(input()):
	arr = [0, 0]

	for i in range(int(input())):
		t = input().split()
		arr[0] += int(t[0])
		arr[1] += int(t[0]) * float(t[1])
	
	print(arr[0], round(arr[1]/arr[0], 1))