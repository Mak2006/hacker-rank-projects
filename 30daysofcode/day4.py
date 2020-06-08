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
            id +=1 # increament the id.
            print("Age is not valid")
        else:
            self.age = initialAge # SET it to the person age


    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")