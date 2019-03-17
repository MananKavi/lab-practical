myList = ['w', 'e', 'l', 'c', 'o', 'm', 'e']
print("Before sort\n", myList)

for index in range(1, len(myList)):

    currentvalue = myList[index]
    position = index

    while position > 0 and myList[position - 1] > currentvalue:
        myList[position] = myList[position - 1]
        position = position - 1

    myList[position] = currentvalue

print("After sort\n", myList)
