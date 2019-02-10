# Program to search an element from a given list
from typing import Any, Union


def SearchFunction(list_of_elements, l, r, x):
    while l <= r:

        mid = int(l + (r - l) / 2)

        if list_of_elements[mid] == x:
            return mid

        elif list_of_elements[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    return -1


listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 80, 90, 100]
x = int(input("Enter an element to be searched : "))

result = SearchFunction(listOfNumbers, 0, len(listOfNumbers) - 1, x)

if result != -1:
    print("Element ", x, " is present at index ", result)
else:
    print("Element ", x, " is not present in array")