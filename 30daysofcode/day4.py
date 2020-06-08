#Day 4: Class vs. Instance
#cLASS definiton
class Person:
    # A class variable, initialized to 0
    id = 0;


    #Constructor, passing initial age
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        #Hec for -ve age and set it 0 and print "Age is not valid"
        # do not like that Person can be created with 0 age !
        if(initialAge < 0 ):
            self.age = 0; #Private variable created
            Person.id = Person.id + 1 # increament the id.
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge # SET it to the person age

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        a = self.age
        if(a < 13):
            print("You are young.")
        elif (a >=13 and a < 18):
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age = self.age + 1;
        #print("setting age{}".format(self.age))


if __name__ == '__main__':
    print(" Give first the number of input, then the inputs")
    t = int(input())
    for i in range(0, t):
        age = int(input())
        p = Person(age)
        p.amIOld()
        for j in range(0, 3):
            p.yearPasses()
        p.amIOld()
        print("")