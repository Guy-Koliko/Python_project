from smallFoot.classFun.dataBaseClass import dataBase
from smallFoot.function.addFunction import addContact as add
from smallFoot.function.deleteFun import deleteContact as delete
from smallFoot.function.searchFun import searchThroughDb as search
from smallFoot.function.showAllContact import showAllContact as show
from smallFoot.function.updateFun import upDateDB as update


def main():
    app = dataBase("contact.data")
    choice = ''
    while choice != '5':
        print(app)
        choice = input('Choose: ')
        if choice == '1':
            add()
        elif choice == '2':
            show()
        elif choice == '3':
            search()
        elif choice == '4':
            update()
        elif choice == '5':
            delete()


if __name__ == '__main__':
    main()
