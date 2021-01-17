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

print("Enter a number:", end=' ')
num = int(input())
print(fizz_buzz(num))