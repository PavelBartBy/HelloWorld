from SUtilities import *
from SCoctails import Coctail
from SIngridient import *
from SMenu import *

class Bar:

    def cash(self):
        x=input("Enter your amount of cash ")
        if check_digit(x)==True:
            return x

    def calculation(self,cash=0):
        print("You can take: ")
        coctail_data=Coctail.read(self,'Coctails.pickle')
        ingridient_data=Ingridient.read(self,'Ingridients.pickle')
        for i in coctail_data:
            if i.get_price()<=cash:
                print(i.coctail_name)
        
    def create_coctail(self):

        new_coctail=Coctail.add_coctail(self)
        print('Your coctail: '+new_coctail.coctail_name
            +" With price: "+str(Coctail.get_price(self,new_coctail))
            +" Volume: "+str(Coctail.get_volume(self,new_coctail))
            +" And alcghohol degree: "+ str(Coctail.get_alc(self,new_coctail)))


"""Create files with ingridients and coctails manually"""
menu=Menu()
#menu.ingridients_to_file()
#menu.coctails_to_file()

"""Create files with ingridients and coctails automatic"""
ingridients_xls=menu.ingridients_fxls(read_xlsfile(r'C:\Users\BART\ShakerProject\Ingridients.xls'))
coctails_xls=menu.coctails_fxls(read_xlsfile(r'C:\Users\BART\ShakerProject\Coctails.xls'))
menu.add('Coctails.pickle',coctails_xls)
menu.add('Ingridient.pickle',ingridients_xls)

new_bar=Bar()
cash=new_bar.cash()
new_bar.calculation(int(cash))
que=input("Or create new coctail? yes/no")
if que=='yes':
    new_bar.create_coctail()
else:
    print('Bye-bye')
    pass

#End