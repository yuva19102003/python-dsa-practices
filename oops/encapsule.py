
class base:

    def __init__(self):

        self.public = "this is a public member"
# "__" double underscore represents private attribute. 
# Private attributes start with "__".
        self.__private = 5  

    def display(self):

        self.private = self.__private
        return self.private


class derived(base):

    def __init__(self):

        base.__init__(self)

        print("calling the private member from the base class")

        a = base.display(self)
        b = 10
        c = a + b
        print(c)

        print("calling the public member from the base class")  
        print(self.public)


derived1 = derived()

