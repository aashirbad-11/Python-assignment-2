# Python Assignment 2

x = 5
for i in range(1, x +1):
	for j in range(1, i +1):
		print('* ', end ='')
	print('')
for i in range(x -1, 0, -1):
	for j in range(1, i + 1):
		print('* ', end = '')
	print('')

'''

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

# 2. Write a Python program to reverse a word after accepting the input from the user.

user_input = input('Enter a word : ')
print(user_input[:: -1])