
def fibnac(n):
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return fibnac(n-1) + fibnac(n-2)


print("Program to print Fibonacci Series of n Numbers.")
n=int(input("N:"))
print(fibnac(n))
