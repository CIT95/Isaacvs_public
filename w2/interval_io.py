while True:
	print('Enter a starting value.')
	start_val = input()
	print('')

	print('Enter a ending value')
	end_val = input()
	print('')

	if int(start_val) > int(end_val):
		print('Error, starting value is greater than ending value.')
		print('Please try again.\n')
	else:
		break

for i in range(int(start_val), int(end_val) + 1):
	print(i)