"""
    This page is a small screen for the terminal program
"""

def screen(a,b,):
    print('CONVERTING %s '%a)
    scn = """"
                     CONVERTING %s
               -------------------------
              *                         *
            *     ____________________    *
            *    |Roman Num | Number  |   *
            *    **********************   *
            *    |          |         |   *
            *    |    %s    |    %s   |   *
            *    **********************   *
            \                             /
             *****************************
           """ %(b,a,b)
    return(scn)
# print(screen(9,800,7))