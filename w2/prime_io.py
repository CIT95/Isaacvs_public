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
	if i == 2 or i == 3:
		print(i)
	elif i % 2 == 0 or i % 3 == 0 or i == 1:
		continue
	else:
		mult = 0
		for j in range(2,  int(i ** .5) + 1):
			if i % j == 0:
				mult = 1
				break
		if mult == 0:
			print(i)