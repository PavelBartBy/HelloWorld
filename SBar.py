from SUtilities import Utilities
from SCoctails import Coctail
from SIngridient import HotDrink,Liquor,Juce,Soda,Syrop
from SMenu import Menu

class Bar:

    def get_cash(self):
        x=input("Enter your amount of cash ")
        if Utilities.check_digit(x)==True:
            return x

    def calculate_recommend(self,cash=0):
        print("You can take: ")
        coctail_data=Coctail.read(self,'Coctails.pickle')
        for i in coctail_data:
            if i.get_price()<=cash:
                print(i.coctail_name)
        
    def create_coctail(self):

        new_coctail=Coctail.add_coctail(self)
        print('Your coctail: %s  With price: %s Volume: %s And alcghohol degree: %s'
                % (new_coctail.coctail_name, str(Coctail.get_price(self,new_coctail)),str(Coctail.get_alc(self,new_coctail)))


"""Create files with ingridients and coctails manually"""

#menu=Menu()
#menu.ingridients_to_file()
#menu.coctails_to_file()

"""Create files with ingridients and coctails automatic from '.csv' file"""

new_bar=Bar()
cash=new_bar.cash()
new_bar.calculate_recommend(int(get_cash))
que=input("Or create new coctail? yes/no")
if que=='yes':
    new_bar.create_coctail()
else:
    print('Bye-bye')
    pass

#End