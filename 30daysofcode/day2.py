#Operators
# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
#
# Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!
#
# Input Format
#
# There are  lines of numeric input:
# The first line has a double,  (the cost of the meal before tax and tip).
# The second line has an integer,  (the percentage of  being added as tip).
# The third line has an integer,  (the percentage of  being added as tax).
#
# Output Format
#
# Print the total meal cost, where  is the rounded integer result of the entire bill ( with added tax and tip).
#
# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    cpst = meal_cost *(1+ (tip_percent + tax_percent)*0.01)
    print(round(cpst));


if __name__ == '__main__':


# asks for 3 inputs, meal cost, tip_percent and tax percent.
# DOes not check for null values.

    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

