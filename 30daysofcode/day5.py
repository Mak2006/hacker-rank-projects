#Loops

#Given an integer, , print its first  multiples.
# Each multiple  (where ) should be printed on a new line in the form: n x i = result.4


def gen_table(num):
    for i in range (1, 11):
        print("{} x {} = {}".format(num, i, num*i))


if __name__ == '__main__':
    n = int(input())
    gen_table(n)