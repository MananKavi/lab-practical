#  Program to count number of occurrence of a character
def count_character(string, char):
	if not string:
		return 0
	elif string[0] == char:
		return 1 + count_character(string[1:], char)
	else:
		return count_character(string[1:], char)


testString = input("Enter a string : ")
testChar = input("Enter a character : ")
count = 0

for i in testString:
	if i == testChar:
		count = count + 1

print("Count of " + testChar + " in " + testString + " is : " + str(count) + " with 'Iteration'")
print("Count of " + testChar + " in " + testString + " is : " + str(
	count_character(testString, testChar)) + " with 'Recursion'")
