#Empty Returns You can also write return without anything afterwards, and this just tells the function to exit.
def format_name(f_name, l_name):
    if f_name=="" and l_name=="":
        return("input valid value")
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AngelA", "YU"))
