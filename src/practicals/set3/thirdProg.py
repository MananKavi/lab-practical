from _datetime import datetime

file = open("student.txt", "r")

for aline in file:
    values = aline.split(" ")
    date_obj = datetime.strptime(values[1], '%m/%d/%Y')
    print("Name : ", values[0], "\nDate Of birth : ", date_obj.strftime('%m-%d-%Y'))
