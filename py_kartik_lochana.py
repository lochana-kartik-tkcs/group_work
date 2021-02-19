def fun1(arr,l,r,x)://~kartik
	#base case
	if r>=1:

		mid=l+(r-1)/ 2;

		if arr[mid]==x:
			return mid

		elif arr[mid]> x:
			return fun1(arr,l,mid-1,x)
		else:
			return fun1(arr, mid+1,r,x)
	else:
		return -1

def fun2(a, b)://~Lochana
	print("Original value of a is", a)
	print("Original value of b is", b)

	temp = a
	a=b
	b=temp
	print("Changed value of a is",a)
	print("Changed value of b is",b)

def fun3(n)://~Lochana
	c=0
	if(n==0 || n==1):
		print("Not prime")
	else:
		for i in range(0, n):
			if(n%i==0):
				c=c+1
		if(c==2):
			print("Number is prime")
		else:
			print("Not prime")
