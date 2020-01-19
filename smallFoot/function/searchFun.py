import os


os.path.exists('../classFun/')

# this function is for the searching through the database

def searchThroughDb():
    search = input("Search : ")
    from smallFoot.classFun.dataBaseClass import dataBase as db

    if search in db.contPersonDir:
        print(db.contPersonDir[search])
    else:
        print('Search does no exist ')