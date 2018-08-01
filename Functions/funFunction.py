# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the
# number of that iteration and specify whether it's an odd or even number.

def odd_even():
    for value in range(1,2001):
        if value % 2 != 0:
            print ("Number is {}.  This is a odd number".format(value))
        if value % 2 == 0:
            print ("Number is {}.  This is a even number".format(value))

odd_even()


# Multiply:
# Create a function called 'multiply' that iterates through each value in a
# list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has
# been multiplied by 5.
# The function should multiply each value in the list by the second argument.

arr = [2,4,10,16]
def multiply(arr, multiple):

    for item in enumerate(arr):
        multiplied = item[1] * multiple
        arr[item[0]] = multiplied
    return arr
b = multiply(arr, 5)
print(b)
