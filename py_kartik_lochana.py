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
