# Write a function that simulates tossing a coin 5,000 times.
# Your function should print how many times the head/tail appears.

import random

def coinToss():
    head = 0
    tail = 0
    print ("Start of program")

    for idx in range (1,5001):
        num = random.randint(0,1)
        if num == 1:
            head += 1
            print ("Attemp #{}: Throwing a coin... It's a head! ... got {} head(s) so far and {} tail(s) so far".format(idx,head,tail))
        else:
            tail += 1
            print ("Attemp #{}: Throwing a coin... It's a tail! ... got {} head(s) so far and {} tail(s) so far".format(idx,head,tail))
    print ("End of program")

coinToss()
