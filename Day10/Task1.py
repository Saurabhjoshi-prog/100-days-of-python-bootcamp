def format_name(f_name,l_name):
    # Use the title() function to modify the f_name and l_name parameters into Title Case.
    f_name=f_name.title()
    l_name=l_name.title()


#You can create a function with a body, input and output like this:
def mood(p_mood):
    if p_mood=="happy":
        return("its good to see you happy today")
    else:
        return("cheer up you got this!")
output=mood(input("how are you feeling right now?"))
print(output)