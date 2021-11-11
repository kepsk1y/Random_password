import random
import string 

def get_random_string():
	length = input("Enter the number of digits of password: ")
	letters = string.ascii_lowercase
	result_str = ''.join(random.choice(letters) for i in range(int(length)))

	print(f"Random string of length {length} is - {result_str}")

get_random_string()
