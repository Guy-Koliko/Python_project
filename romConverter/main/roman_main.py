"""
    This is a simple program that takes in a number
    and shows the Roman numeral part of that number
"""
from romConverter.classes import RomanClass as rn
from romConverter.functions import banner as bn
from romConverter.functions import screen as sn

def inputs():
    tn = int(input("Enter Your Number : "))
    runprograme = rn.Roman.display(tn)
    return (runprograme)


def _main():
    bn.banner()
    inputs()

_main()