
class bird:

    def origin(self):
        print("this is a bird")

class parrot(bird):

    def name(self):
        print("this is a parrot")

class crow(bird):
    
    def name(self):
        print("this is a crow")


bird1 = bird()
bird1.origin()

parrot1 = parrot()
parrot1.name()
parrot1.origin()

crow1 = crow()
crow1.name()
crow1.origin()
