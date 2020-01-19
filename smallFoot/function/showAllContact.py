import os


def showAllContact():
    from smallFoot.classFun.dataBaseClass import dataBase as db
    # this part of the system prints all the contact we have in place
    if db.contPersonDir:
        e = """
            ===================================================================
            |{}                | {}               | {}               |
            ====================================================================
                """
        print(e.format('FIRST NAME', 'LAST NAME', 'PHONE NUMBER'))

        if db.contPersonDir in db.contPersonDir.values():
            print(db.contPersonDir)
        else:
            print("No contact found")