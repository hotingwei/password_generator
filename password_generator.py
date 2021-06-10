import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")
number_of_letters = int(input(f"How many letters would you like in your password : \n"))
number_of_numbers = int(input(f"How many numbers would you like: \n"))
number_of_symbols = int(input(f"How many symbols would you like: \n"))

#Eazy Level (with sequence)

password = ""
for letter in range(1, number_of_letters + 1):
	letter = random.choice(letters)
	password = password + letter
	# quicker solution that will replace line 15, 16: password += random.choice(letters)
for number in range(1, number_of_numbers + 1):
	number = random.choice(numbers)
	password = password + number
	# quicker solution: same as letter part
for symbol in range(1, number_of_symbols + 1):
	symbol = random.choice(symbols)
	password = password + symbol
	# quicker solution: same as letter part
print(password)

#Hard Level (Random)
password_hard = []

for letter in range(1, number_of_letters + 1):
	password_hard.append(random.choice(letters))
for number in range(1, number_of_numbers + 1):
	password_hard.append(random.choice(numbers))
for symbol in range(1, number_of_symbols + 1):
	password_hard.append(random.choice(symbols))

random.shuffle(password_hard)
password_generator = ""
for char in password_hard:
	password_generator += char

print(f"Your password is: {password_generator}")