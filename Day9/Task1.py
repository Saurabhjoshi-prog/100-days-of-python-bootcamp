programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
# to retrive items from the dictionary
print(programming_dictionary["Bug"])
# to create an empty dictionary
happy={}
# to add new items in the dictionary
programming_dictionary["peach"]="pink"
print(programming_dictionary)
#to edit the dictionary
programming_dictionary["peach"]="red"
print(programming_dictionary)
# how to loop through all values in a dictionary
for i in programming_dictionary:
    print(i)
for i in programming_dictionary:
    print(programming_dictionary[i])