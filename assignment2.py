def fib(n):

    # This function will compute and return
    # the nth fibonacci number. Unless the 
    # the vaule is negative, then it return None.
	# We will start be writing an if statement 
	
	if n <= 0:
		return None
	elif n == 1 or n == 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

