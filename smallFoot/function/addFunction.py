import os.path

os.path.exists('../constructor/')
os.path.exists('../classFun/dataBaseClass.py')


def addContact():


    from smallFoot.classFun.dataBaseClass import dataBase as db
    from smallFoot.constructor.PersonConstructor import Person
    from smallFoot.function.inputFun import inputContact

    dbs = db(None)

    firstName, lastName, phoneNumber = inputContact()
    if firstName not in dbs.contPersonDir:
        dbs.contPersonDir[firstName] = Person(firstName, lastName, phoneNumber)
    else:
        print('CONTACT EXIT')
