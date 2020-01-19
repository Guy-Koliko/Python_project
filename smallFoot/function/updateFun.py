import os

#
from smallFoot.function.inputFun import inputContact as inp

def upDateDB():
    from smallFoot.classFun.dataBaseClass import dataBase as db
    update = input("Update : ")

    if update in db.contPersonDir:
        print("Entry Found. Prepare to update records ...... ")
        firstname,lastname,phonenumber = inp()
        db.contPersonDir[update]=(firstname,lastname,phonenumber)
        print('Successfully updated')
    else:
        print('Contact not found.')
