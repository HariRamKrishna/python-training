def fibo(num):
	a, b = 0, 1
	while num:
		print(a)
		a, b = b, a+b
		num=num-1


fibo(100)
