import os
from smallFoot.classFun.dataBaseClass import dataBase as db

def deleteContact():
    deletename = input('Delete name : ')
    if deletename in db.contPersonDir:
        del db.contPersonDir[deletename]
        print('Contact has been successfully deleted.')
    else:
        print('Contact not found')