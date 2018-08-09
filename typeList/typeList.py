#input
mylist = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"



def filterType(arg):
    sum = 0
    for index in arg:
        if  isinstance(index, str):
                print ("The list you entered is of mixed type : {}".format(index))
        if  isinstance(index, int):
                print ("add in sum : {}".format(index))


filterType(mylist)
