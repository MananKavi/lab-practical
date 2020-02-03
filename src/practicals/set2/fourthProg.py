# Python program to check if the number provided by the user is an Armstrong number or not
number = int(input("Enter a number: "))
order = len(str(number))
sumOfNumber = 0

temp = number
while temp > 0:
	digit = temp % 10
	sumOfNumber += digit ** order
	temp //= 10

if number == sumOfNumber:
	print(number, "is an Armstrong number")
else:
	print(number, "is not an Armstrong number")
