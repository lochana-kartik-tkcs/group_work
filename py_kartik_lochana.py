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
