import random
import string 

characters = string.ascii_letters + string.digits

def get_random_string():
	length = input("Enter the number of digits of password: ")
	result_str = ''.join(random.choice(characters) for i in range(int(length)))

	print(f"Random string of length {length} is - {result_str}")

get_random_string()
