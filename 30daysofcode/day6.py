# Given a number of strings, print the odd chars space even cars
def candyprint(givenstrings):

    for i in range(0, len(givenstrings)):
        acandy = givenstrings[i]
        even = ""
        odd = ""
        for j in range(0, len(acandy)):
            if(j%2 ==0):
                even += acandy[j]
            else:
                odd += acandy[j]
        print(even + " " + odd)


    pass #for i in range(0, )


def check(givenstrings):
    for i in range(0, len(givenstrings)):
        print(i)
        print(givenstrings[i])


if __name__ == '__main__':

    numofinput = input()
    #ALl the inptus are taken at onece7
    givenstrings = [] # require an array of strings
    for i in range (0, int(numofinput)):
        givenstrings.append(input())

    #at this stage the string should be in the ds
    #check(givenstrings)

    candyprint(givenstrings)
