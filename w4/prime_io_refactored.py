while True:
	# get starting value
	print('Enter a starting value.')
	start_val = input()

	# get ending value
	print('Enter a ending value')
	end_val = input()

	# check if starting is bigger that ending
	# starts loop again if true
	try:
		if int(start_val) > int(end_val):
			print('Error, starting value is greater than ending value.')
			print('Please try again.\n')
		else:
			break
	except ValueError:
		print('Error, did not enter a number')
		print('Please try again.\n')

#print primes
print('Primes:')
for i in range(int(start_val), int(end_val) + 1):
	# check for 2 or 3 which are primes
	if i == 2 or i == 3:
		print(i)
	# check if i is divisible by 2 or 3, or is 1
	# if true i is not prime and continue loop
	elif i % 2 == 0 or i % 3 == 0 or i == 1:
		continue
	# loop through numbers 4 to the square root of i
	# if i is divisible by j, i is a prime number
	# print i if mult is equal to 0
	else:
		mult = 0
		for j in range(4,  int(i ** .5) + 1):
			if i % j == 0:
				mult = 1
				break
		if mult == 0:
			print(i)