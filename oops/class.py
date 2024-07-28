

# CLASS AND OBJECTS

# class name
class Dsec:
    # class  attributes
    dept = "CSE"
    # instances which will execute whenever the class name is called
    def __init__ (self, name):
        self.name = name


# object

student = Dsec("student")
staff = Dsec("staff")

# calling the class attributes and class members in object
print(student.dept)
print(student.name)
print(staff.name)