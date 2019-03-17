class Student:
    def set_data(self):
        self.rollno = int(input("Enter roll no. : "))
        self.name = str(input("Enter name : "))
        self.age = int(input("Enter Age : "))
        self.t_marks = int(input("Enter total Marks :"))

    def get_data(self):
        print("Roll no", self.rollno)
        print("Name ", self.name)
        print("Age ", self.age)
        print("Total Marks", self.t_marks)

    def __eq__(self, other):

        if self.t_marks == other.t_marks:
            self.p = 1
        else:
            self.p = 0

        return self.p


student = []
numberOfStudents = int(input("Enter the number of student : "))
for i in range(0, numberOfStudents):
    student.append(Student())

for i in range(len(student)):
    student[i].set_data()

for i in range(len(student)):
    for j in range(i + 1, len(student)):
        t = (student[i] == student[j])
        if t == 1:
            print("\n Student detail having same marks :\n")
            student[i].get_data()
            student[j].get_data()
