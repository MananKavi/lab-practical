num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
num3 = int(input("enter third number : "))

if num1 == num2 and num1 == num3:
    total = 3*num1
else:
    total = num1 + num2 + num3

print(str(total)+" is total of three number.")