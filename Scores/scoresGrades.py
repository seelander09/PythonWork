# # Write a function that generates ten scores between 60 and 100.
# Each time a score is generated, your function should display what
# the grade is for a particular score. Here is the grade table:
# #
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
import random

def scoresAndGrades():

    for value in range(0,10):
        randNum = random.randint(60,100)
        if randNum >= 90:
            print ("Score: {}; Your grade is A".format(randNum))
        elif randNum >= 80:
            print ("Score: {}; Your grade is B".format(randNum))
        elif randNum >= 70:
            print ("Score: {}; Your grade is C".format(randNum))
        elif randNum >= 60:
            print ("Score: {}; Your grade is D".format(randNum))

scoresAndGrades()
