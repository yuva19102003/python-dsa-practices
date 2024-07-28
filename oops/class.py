

# CLASS AND OBJECTS

# class name
class Dsec:
    # class  attributes
    dept = "CSE"
    # instances which will execute whenever the class name is called
    def __init__ (self, name):
        self.name = name

    def speak(self):
        print("this is a {} from department of {}".format(self.name, self.dept))


# object

student = Dsec("student")
staff = Dsec("staff")

# calling the class attributes and class members in object
print(student.dept)
print(student.name)
print(staff.name)

# calling the class method in object
student.speak()
staff.speak()