def binary_search(searchList, item):
    if len(searchList) == 0:
        return False
    else:
        mid = len(searchList) // 2
        if searchList[mid] == item:
            return True
        else:
            if item < searchList[mid]:
                return binary_search(searchList[:mid], item)
            else:
                return binary_search(searchList[mid + 1:], item)


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
element = int(input("Enter element to be searched : "))

if binary_search(myList, element):
    print("Element found!")
else:
    print("Element not found!")
