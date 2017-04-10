# problem 1

# this variable collects the sum of all the numbers divisible by 3 or 5
numberSum = 0

for n in range(0,1000):
	print n

	# test for divisibility
	if (n % 3 == 0) or (n % 5 == 0):
		print '%d is divisible by 3 or 5' % n
		# add the term that is divisible by 3 or 5 to the sum variable
		numberSum = numberSum + n
		print '** the new numberSum is %d' % numberSum
	else:
		print '%d is NOT divisible by 3 or 5' % n
