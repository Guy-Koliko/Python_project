"""
    This is a simple program that takes in a number
    and shows the Roman numeral part of that number
"""
from romConverter.classes import RomanClass as rn


def inputs():
    tn = int(input("Enter Your Number : "))
    runprograme = rn.Roman.display(tn)
    return (runprograme)

def banner():
    b ="""
    *******************************************
    *  WELCOME TO THE ROMAN NUMERAL CONVECTOR *
    *******************************************
"""
    print(b)

def _main():
    banner()
    inputs()

_main()