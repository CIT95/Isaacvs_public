def dupString(string='', times=0):
	if len(string) == 0 or times == 0:
		print("No duplication then?")
		return
	newString = string
	for i in range(times):
		newString = newString + string
	return newString

	

def stringMulti():
	print('Enter string for duplication:', end=' ')
	string = input()
	print('Enter number of times to be duplicated:', end=' ')
	num = int(input())

	# I have the same code inside of dupString for the purpose of demostrating default params
	# could have avoided code like this
	if len(string) == 0 or num == 0:
		dupString()
		return
	newString = dupString(string, num)
	print(newString)

stringMulti()