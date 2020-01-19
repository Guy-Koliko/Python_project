"""
This is the part of the database constructor that
starts how the database will handle the item.
Here a lot goes on. For things to be written to the database it all comes from here
"""

import os
import pickle

# from smallFoot.ui.ui import menu

class dataBase(object):


    menu = '''
            X-----------------------X
            | 1. Add New Contact    |
            | 2. Update Contact     |
            | 3. View All Contact   |
            | 4. Delete Contact     |
            | 5. Rest All Contact   |
            | 6. Search A Contact   |
            | 7. Exit               |
            X-----------------------X
           '''

    contPersonDir = {}
    path = os.path

    # constructor for the dataBase
    def __init__(self,db):
        self.db = db


    def __int__(self,db):
        self.dbase = db
        if self.path.exists(self.db):
            writeToDb = open(self.dbase, 'wb')
            pickle.dump({},writeToDb)
            writeToDb.close()
        else:
            with open(self.dbase, 'rb')as wdb:
                self.contPersonDir = pickle.load(wdb)

    def __str__(self):
        return self.menu
