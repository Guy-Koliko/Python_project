# importing the roman function

from romConverter.functions import roman_function as rn


# building the Roman class
class Roman:

    # building the constructor for our class
    def __init__(self,num):
        self.num = num

    # building the display object to display our numerals
    def display(self):
        print(rn.conVertNumber(self)," STAND FOR ", self)
