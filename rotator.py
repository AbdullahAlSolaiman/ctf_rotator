# This is an easy implementation of Ceaser Cipher and could be replaced
# for any roatation-based cipher such as rot13, etc.

import string
import collections
import pyfiglet

# Function that takes the string to be rotated + the number of digits to be shifted
# example usage: shift_rotate(string, 13) ---> for ROT13

def shift_rotate(string_to_rotate, num_of_rotations):
    # creating a list of upper and lower case letters
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    # rotating by num of rotations
    upper.rotate(num_of_rotations)
    lower.rotate(num_of_rotations)

    # converting the list into a string
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    return string_to_rotate.translate(string.maketrans(string.ascii_uppercase, upper).translate(string.maketrans(string.ascii_lowercase, lower)))


# Creating the banner

ascii_banner = pyfiglet.figlet_format("Rotator")
print(ascii_banner)

print("Welcome, Please Enter the following Details: ")

choice = input('[1] Decode by N Rotations\n[2] Show all 26 possible rotations\n[3] Exit The Program\nChoice----------> ')

if (choice == 1):
	string_to_rotate = raw_input("Enter the string you wanna rotate: ==> ")
	num_of_rotations = input("How many rotations you want? ===> ")

	print("===============================================")
	print("                 Before Decoding               ")
	print ("==============================================")
	
	print(string_to_rotate)

	print("\n\n===============================================")
	print("                 Before Decoding               ")
	print ("==============================================")
	decoded = shift_rotate(string_to_rotate,num_of_rotations)
	print(decoded)

elif (choice == 2):
	string_to_rotate = raw_input("Enter the string you wanna rotate: ==> ")
	for i in range(0,26):
		decoded = shift_rotate(string_to_rotate, i) 	
		print("["+ str(i) + "]  " + decoded)

elif (choice == 3):
	exit()
else:
	print("invalid input... shutting down")
