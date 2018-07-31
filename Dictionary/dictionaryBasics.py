'''
Create a dictionary containing some information about yourself.
The keys should include name, age, country of birth, favorite language.
Write a function that will print something like the following as it executes:
'''

# My name is Chad
# My age is 32
# My country of birth is The United States
# My favorite language is Python


def printAboutMe(dic):
    print ("My name is {}".format(dic['name']))
    print ("My age is {}".format(dic['age']))
    print ("My country of birth is {}".format(dic['birthCountry']))
    print ("My favorite language is {}".format(dic['favLanguage']))

aboutMe = { "age" : "32", "birthCountry" : "USA", "favLanguage" : "Python","name" : "Chad" }

printAboutMe(aboutMe)
