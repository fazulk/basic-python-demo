#compares two numbers based upon user input and returns a a statmentn declaring which number is greater than the other. Basic!  I know. Just getting a feel for the way functions work in python. 

print "This will compare two numbers, and tell you which is greater or less than the other\n"
number_1 = raw_input("Enter the first number\n")
number_2 = raw_input("Enter the second number\n")

cmp_val = cmp(number_1, number_2)
if cmp_val < 0:
	print(number_1 + " is less than " + number_2)
elif cmp_val == 0:
	print("They are the same number!")
else:
	print(number_1 + " is greater than " + number_2)
