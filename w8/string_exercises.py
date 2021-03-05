# String exercises

# pynative.com
# Exercise 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
str2 = "DoEs IT worK"

def lower_first(string):
	newstr = ""
	for elem in string:
		if elem.islower():
			newstr += elem
	for elem in string:
		if elem.isupper():
			newstr += elem

	return newstr

print(lower_first(str1))
print(lower_first(str2))
print("")
# Easy difficulty. Solved without help

# Exercise 7: String characters balance Test
# We’ll assume that a String s1 and s2 is balanced if all the chars in the s1 are there in s2.
# characters’ position doesn’t matter.
def balanced(str1, str2):
	for elem in str1:
		if elem not in str2:
			return False

	return True

# test 1
s1 = "Yn"
s2 = "PYnative"
print(balanced(s1, s2))
# test 2
s1 = "Ynf"
s2 = "PYnative"
print(balanced(s1, s2))
d = 2
d += 2
print("")
# Easy difficulty. Solved without help

# Exercise 8: Find all occurrences of “USA” in a given string ignoring the case
def count_of_usa(string):
	temp_str = string.lower()
	count = 0
	p = 0

	while p < len(temp_str):
		if temp_str[p] == 'u':
			if temp_str[p + 1] == 's' and temp_str[p + 2] == 'a':
				count = count + 1
				p += 3
				continue
		p += 1

	print("The USA count is: " + str(count))

# test 1
str1 = "Welcome to USA. usa awesome, isn't it?"
count_of_usa(str1)
# test 2
str2 = "Welcome to USA. usa awesome, isn't it? UsA maybe not as good as us says."
count_of_usa(str2)
print("")
# Good challenge difficulty.
# Initially I looked up string functions to see if there was one that returns count of a value inside a string,
# there was so to make the question more difficult, I solved without using count()

# Exercise 11: Reverse a given string
def reverse_str(string):
	temp_str = ""
	p = -1

	for char in string:
		temp_str += string[p]
		p -= 1

	return temp_str

str1 = "PYnative"
str2 = "New York"
print(reverse_str(str1))
print(reverse_str(str2))
print("")
# Easy difficulty. Solved without help

# Exercise 13: Split a given string on hyphens into several substrings and display each substring
def spilt_str(string):
	sub_strs = []
	temp_str = ""

	for char in string:
		if char == '-':
			sub_strs.append(temp_str)
			temp_str = ""
		else:
			temp_str += char
	if len(temp_str) > 0:
		sub_strs.append(temp_str)

	for elem in sub_strs:
		print(elem)

str1 = "Emma-is-a-data-scientist"
str2 = "I-go-to-fresno-city-college"
spilt_str(str1)
spilt_str(str2)
print("")
# Medium difficulty. Solved without using split() and without help



# https://www.w3resource.com/python-exercises/string/
# 25. Write a Python program to create a Caesar encryption.
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V',
		'W', 'X', 'Y', 'Z']

def encrypt(shift, string):
	global alph
	cipher = alph[-shift:]
	encrypted_str = ""

	for i in range(0, len(alph) - shift):
		cipher.append(alph[i])

	print(cipher)

	for char in string.upper():
		if char.isalpha():
			encrypted_str += cipher[alph.index(char)]
		else:
			encrypted_str += char

	print(encrypted_str)
	print("")

encrypt(3, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
# Good challenge difficulty.
# I was pretty confused while solving this problem because it was never really explained whether the cipher was
# supposed to be shifted to the left or right, so I decided to go with a left shift.
# This means that 'D' would become 'A'. Solved without help

# 40. Write a Python program to reverse words in a string.
def reverse_word(string):
	p = -1
	new_str = ""

	for char in string:
		new_str += string[p]
		p -= 1

	return new_str

def reverse_words(string):
	new_str = ""
	temp_str = ""

	for char in string:
		if not (char.isalpha()):
			new_str += reverse_word(temp_str) + " "
			temp_str = ""
		else:
			temp_str += char

	if len(temp_str) > 0:
		new_str += reverse_word(temp_str)

	print(new_str)
	print("")

reverse_words("Reverse the words in this string")
# Medium difficulty.
# I thought the problem was asking to reverse each word in the string,
# but after looking at the solution they meant to reverse the order of the words in the string.
# So technically its not the way they wanted but I'll leave it because it was still good
# Solved without help.

# 58. Write a Python program to move spaces to the front of a given string.
def spaces_to_front(string):
	spaces = ""
	chars = ""

	for char in string:
		if char == " ":
			spaces += char
		else:
			chars += char

	new_str = spaces + chars
	print(new_str)
	print("")

spaces_to_front("Move   The   Spaces To The Front  ")
# Medium difficulty. Solved without help

# 59. Write a Python program to find the maximum occurring character in a given string.
def find_max_char(string):
	char_counts = {}
	max_key = string[0]

	for char in string:
		if char.isalpha():
			char_counts.setdefault(char, string.count(char))

	for key in char_counts:
		if char_counts[key] > char_counts[max_key]:
			max_key = key

	print("Maximum occuring character: " + max_key)
	print("")

find_max_char("What is the maximum occuring character?")
# Medium difficulty. Solved without help

# 66. Write a Python program to make two given strings (lower case, may or may not be of the same length)
# anagrams removing any characters from any of the strings.
def make_anagram(str1, str2):
  char1_count = {}
  char2_count = {}
  
  for char in str1:
    if char.isalpha():
      char1_count.setdefault(char, str1.count(char))
    
  for char in str2:
    if char.isalpha():
      char2_count.setdefault(char, str2.count(char))
    
  new_str1 = ""
  new_str2 = ""
  
  for char in str1:
    if char in char2_count and new_str1.count(char) < min(char1_count[char], char2_count[char]):
      new_str1 += char
      
  for char in str2:
    if char in char1_count and new_str2.count(char) < min(char1_count[char], char2_count[char]):
      new_str2 += char
  
  print("New strings: " + new_str1 + ', ' + new_str2)
  
make_anagram("in a race", "a career")
# Good challenge difficulty. Solved without help