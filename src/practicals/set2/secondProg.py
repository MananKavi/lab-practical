# Program to generate fibonacci sequence.
numberOfTerms = int(input("Enter number of terms : "))
numberOne = 0
numberTwo = 1
count = 0

if numberOfTerms <= 0:
	print("Please enter a positive integer")
elif numberOfTerms == 1:
	print("Fibonacci sequence up to ", numberOfTerms, ":")
	print(numberOne)
else:
	print("Fibonacci sequence up to ", numberOfTerms, ":")
	while count < numberOfTerms:
		print(numberOne, end=' , ')
		nth = numberOne + numberTwo
		numberOne = numberTwo
		numberTwo = nth
		count += 1
