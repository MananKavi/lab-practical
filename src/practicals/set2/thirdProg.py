fileName = str(input("Enter file name : "))
data = input("Enter data to be appended in File :\n")

with open(fileName,"a") as writingFile:
	writingFile.write(data)
with open(fileName,"r") as readingFile:
	print(readingFile.read())
