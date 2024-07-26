from helper import d

# Strings in python 

# strings are Imutable: Once created,their content cannot be changed.
# You can reassign the variable name to a new string, but the original data remains unchanged.

my_string = "Hello, World!"
print(id(my_string))

my_string = "Hello, Python!"
print(id(my_string))

#-- Indexing into string : access individual letters in a string

frist_char = my_string[0]
print(frist_char)

#-- Slicing : you can grab a chunk of a string(substring) using slicing

substring = my_string[0:5]
print(substring)

#-- Iterating : you can iterate over a string to access each character

for char in my_string:
    print(char)


#-- formatted strings

#-- using.format() method
name = "Alice"
formatted_str = "Hello, {}".format(name)
print(formatted_str)

#-- using f-strings
formatted_str = f"Hello, {name}!"
print(formatted_str)


#-- Useful string methods

#-- len() : returns the numbers of characters in a string, or the legth of an iterable 
test = "How many CHARACTERS are in this string?"
print(len(test))

#-- upper() : returns a full upper case version of a given string
print(test.upper())

#-- lower() : returns a full lower case version of a given string
print(test.lower())

#-- isupper() : returns True or False if all characters in a string are uppercase or not
txt = "THS IS NOW!"
print(txt.isupper())

#-- .title() : returns string in title case, capitalizing evry word that is sepertaed by a space 
person = "abraham lincoln"
print(person.title())

#-- .replace(<thing to replace>, <what to replace with>) : replace a substring with a new value 
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print("Using replace():", x)

new_txt = ''
words = txt.split()
print(words)
for word in words:
    print(word)
    if word == 'bananas':
        new_txt += "apples "
    else:
        new_txt += word 

print("Using a loop: ", new_txt)

#-- .lstrip(), .rstrip(), .strip() : allows us to strip whitespace (empty space) out of a string
test = "            Wow this is awesome!!!!     stuff          "
print(test)

left_strip = test.lstrip() #strip the whitespce on the left side of the string only
print(left_strip)

right_strip = test.rstrip() #strip the whitespaces on the right side of the string only
print(right_strip)

reg_strip = test.strip() #strip whitespaces from both sides of a string
print(reg_strip)

#-- " ".join() : joins a list of strings together to form one single string
words = ["Let's", 'join', 'these', 'words', 'together']
joined = " ".join(words)
print(joined)
another_join = "     @@@    ".join(words)
print(another_join)

#-- .find() : search for word in a string and will return the index that the word starts at 
txt = "Hello, welcome to my world!"
found = txt.find("welcome")
print(found)

#-- .count() : counts the occurances of a substring in the main string 
txt = "Foxy Brown is a foxy lady. Is she actually a fox? idk maybe we should ask a real fox?"
print(txt.lower().count("fox"))

#-- .startswith(<substring>) : returns a True or False depeding on wether a string starts with a specified substring

people = ["Tyler", "Jermiah", "Jeremain", "Jasmin", "Brian", "Travis", "Dylan"]
j_team = []
for person in people:
    if person.lower().startswith("j"):
        j_team.append(person)

print(j_team)

#-- .endswith() : returns a True or False depeding on wether a string ends with a certain substring or not
name = "Travis"
print(name.endswith("s"))

#-- .isaplha() : returns True if the string is made ENTIRELY of alphabetic characters
letters = 'asdfghjkl'
print(letters.isalpha())

#-- .isdigit() : returns True if the string is made ENTIRELY of numeric characters
nums = '1234567890'
print(nums.isdigit())

#-- .issapace() : returns True if aa string is comprised solely of whitespace 
empty_space = '         '
print(empty_space.isspace())

#-- .split() : splits your string based on a specific substring into a list of strings, default split is on spaces
words = 'this-is-one-big string with many words'
words_list = words.split()
print(words_list)

words_lists = words.split('-')
print(words_lists)

# flavors = input("tell me all your favorite flavors (separated by space please): ").split()
# print(flavors)

d()

# come back to this - splitting when mulitple characters are involved, not just spaces

words = 'this-is-one-big string with many words'
words_list = words.split()
print(words_list)

complete_list = []

for word in words_list:
    complete_list.append(word.split('-'))

print(complete_list)            