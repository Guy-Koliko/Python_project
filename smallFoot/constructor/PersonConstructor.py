"""
This is a class that define how the person will be updated.
This class contain a constructor that showcase user update.

Author : Guy Koliko
Email  : ubnt5050win@gmail.com
Whatsapp : +233(0)261208893

"""
import os

class Person(object):

    # variables used for the constructor
    firstname = None
    lastname = None
    phonenumber = None
    sex =None
    address = None
    geolocation =None
    fathername =None
    mother=None
    middlename = None

    # this is the constructor for the contactbook

    def __init__(self,first_name,last_name,phone_number):
        self.firstname=first_name
        self.lastname=last_name
        self.phonenumber=phone_number


    def __str__(self):
        return '{}  {}  {}'.format(self.firstname,self.lastname,self.phonenumber)
