from helper import d

# In python there are only two types of issues that will break your code
#-- stop your code from functions or executing, and throw an error

# syntax Errors : errors in your coding grammar, a structural error
#---- misspelling
#--- indentation error
#--- code structure is missing something
#--- colons, indentation, parenthesis, ' ', " "

# Exeptions : arise when our code is stuctured correctly, but some operation doesn't execute for a varaity of reasons 

#-- ZeroDivisionError : occurs when you try to divide by 0
qoutient = 10/0

#-- NameError : trying to call a variable or function before it has been defined
print(x)
print(divi())
def divi():
    pass

#--- ValueError : trying to preform operaations with invalid values 

str_num = 'nine'
int_num = int(str_num) # trying to convert an invalid values

#--- TypeError : trying to perform operations on values of inappropriate types

num = 5
total_people = num + "people" # cannot concentrate a str and an int together 

#--- AttributeError : trying to use methods on improper objects

word = "hello"
word.append("there")


word = "hello"
rword = word.reversed()