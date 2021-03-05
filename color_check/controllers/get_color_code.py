# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.

def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.

    import json

    with open('color_check/data/css-color-names.json') as database_color:
        data_dico = json.load(database_color)
    
        if color_name in data_dico:
            hex_code = data_dico[color_name]
        return hex_code    
        
        
# else:
#      raise Exception
