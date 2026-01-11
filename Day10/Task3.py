"""You can use docstrings to write multiline comments that document your code."""


def format_name(f_name, l_name):
    """this program converts the first and second name to proper format"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")
print(formatted_name)





