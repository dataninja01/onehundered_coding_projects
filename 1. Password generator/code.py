#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
# person_to_pay = random.choice(names)

for l in letters:
    password.append(l)
    if len(password) == nr_letters:
        for n in numbers:
            password.append(n)
            if len(password) == (nr_letters + nr_numbers):
                for s in symbols:
                    password.append(s)
                    if len(password) == (nr_letters + nr_numbers + nr_symbols):
                        print(password)
print(password)
###Simple way
password = ''
for char in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password += random_letter
for sym in range(1, nr_symbols+1):
    random_symbol = random.choice(symbols)
    password += random_symbol
for num in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number
print(password)

###Hard way
password_list = []
for char in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password_list.append(random_letter)
for sym in range(1, nr_symbols+1):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)
for num in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password_list.append(random_number)
# password = password_list.shuffle()
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for p in password_list:
    password += p
print(f'Your password is {password}')
