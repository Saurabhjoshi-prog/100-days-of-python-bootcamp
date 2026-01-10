# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
def greet_with(name,location):
    print(f"hello {name}")
    print(f"What is it like in {location}")
print("with positional arguments:")
greet_with("ranikhet","saurabh")
print("with keyword arguments:")
greet_with(name="saurabh",location="ranikhet")

