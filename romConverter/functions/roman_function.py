
set_of_roman_numerials = {
    1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",11:"XI",12:"XII",13:"XIII",14:"XIV",15:"XV",16:"XVI",
   }



def conVertNumber(num):
    #going through the dictonary

    for key, value in set_of_roman_numerials.items():

        if key == num:
            return value
        elif key == None:
            return "Sorry"