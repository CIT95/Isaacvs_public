while True:
	# get starting value
	print('Enter a starting value.')
	start_val = int(input())
	print('')

	# get ending value
	print('Enter a ending value')
	end_val = int(input())
	print('')

	# check if starting is bigger that ending
	# starts loop again if true
	if int(start_val) > int(end_val):
		print('Error, starting value is greater than ending value.')
		print('Please try again.\n')
	else:
		break

#print numbers
for i in range(int(start_val), int(end_val) + 1):
	print(i)