# fizz_buzz function
def fizz_buzz(num):
	if num % 3 == 0 and num % 5 == 0:
		return 'FizzBuzz'
	elif num % 3 == 0:
		return 'Fizz'
	elif num % 5 == 0:
		return 'Buzz'
	else:
		return num

while True:
	print("Enter a number:", end=' ')
	try:
		num = int(input())
	except ValueError:
		print('Hey! Enter a number next time!')
	else:
		print(fizz_buzz(num))
		break;