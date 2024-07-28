
# parent class
class person(object):

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):

        print("this is display from person class")
        print(self.name)
        print(self.id)

# child class

class detials(person):

    def __init__(self, name, id, dept):
        self.dept = dept
        person.__init__(self, name, id)

    def displaydetials(self):

        print("this is display from detials class")
        print(self.name)
        print(self.id)
        print(self.dept)
        print("calling the display method from person class")
        person.display(self)


# object
person1 = person("person1", 1)
person1.display()

detials1 = detials("detials1", 2, "CSE")
detials1.displaydetials()
detials1.display()