'''Write a program that prints a 'checkerboard' pattern to the console.
Your program should require no input and produce
console output that looks like so:
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
Each star or space represents a square. On a traditional checkerboard
 you'll see alternating squares of red or black. In our case we will
 alternate stars and spaces. The goal is to repeat a process several times.
This should make you think of looping. '''

def checkerboard():
    for i in range(0, 8):
        if i % 2 == 0:
            print ("* " * 4)
        else:
            print (" *" * 4)

checkerboard()
