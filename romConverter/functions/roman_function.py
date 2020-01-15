from romConverter.db import db as d

set_of_roman_numerials=d.db()

def conVertNumber(num):
    #going through the dictonary

    for key, value in set_of_roman_numerials.items():

        if key == num:
            return value
        elif key == None:
            return "Sorry"