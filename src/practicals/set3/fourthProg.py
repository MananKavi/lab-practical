item = str(input("Enter comma separated sequence of words : "))

for word in item:
    word = item.split(",")

thistuple: tuple = (word)

print(sorted(word))

print(thistuple)
