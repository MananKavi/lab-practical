# Program to check that whether number is odd or even.
number = input("Enter an integer : ")

if int(number) % 2 == 0:
	print("Entered number " + str(number) + " is even")
else:
	print("Entered number " + str(number) + " is odd")
