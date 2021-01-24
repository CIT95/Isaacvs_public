while True:
	print('Enter e to exit loop')
	try:
		val = input()
		if val == 'e':
			break
	except KeyboardInterrupt:
		print('Error. Cannot exit loop with keyboard interrupt')