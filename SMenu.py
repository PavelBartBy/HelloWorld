from SIngridient import Ingridient
from SIngridient import HotDrink,Liquor,Juce,Soda,Syrop
from SCoctails import Coctail


class Menu(Ingridient):

    def ingridients_to_file(self):
        libs={'HotDtink': HotDrink.add_hotdrink(self)
            , 'Liqour': Liquor.add_liqour(self)
            , 'Soda': Soda.add_soda(self)
            , 'Syrop': Syrop.add_syrop(self)
             }
        ingridient_dict={}
        j=0
        x=''
        while x!='stop':
            x=input("Choose type of ingridient: HotDrink, Liqour, Juce, Soda, Syrop  or stop ")
            for i in libs.keys():
                if x==i:
                    ingridient_dict[j]=libs.get(i)
                    j+=1
        self.write(ingridient_dict)           
   
    def coctails_to_file(self):
        coctails_list=[]
        while True:
            x=input('Add new coctail? yes/no ')
            if x=='yes':
                coctails_list.append(Coctail.add_coctail(self))
            if x=='no':
                break
        Coctail.write(self, coctails_list)


