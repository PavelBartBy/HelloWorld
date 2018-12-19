import pickle
from ShakerInterface import IShaker
from SUtilities import Utilities,ReadersFactory


class Ingridient(IShaker):

    def __init__(self,*args, **kwargs):
        super.__class__.__init__()
    
    def read(self,file_name):
        data_new=ReadersFactory.read(self,file_name)
        return data_new
    
    def show(self,file_name):
        ingridient_dict=self.read(file_name)
        for i,j in ingridient_dict.items(): 
            print(i+ ' '+ j.ingridient_name)
    
    def write(self,data):
        with open('ingridients.pickle', 'wb') as f:
            pickle.dump(data, f)
    
    # def check_ingridienttype(self,ingr):
    #     """Check that add Alchohol or NoAlchohok ingridient"""
    #     if Alchohol in ingr.__bases__:
    #         return 1
    #     else:
    #         return 0

class Alchohol(Ingridient):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price,ingridient_alc):
        super().__init__(self)
        self.ingridient_name=ingridient_name
        self.ingridient_volume=ingridient_volume
        self.ingridient_price=ingridient_price
        self.ingridient_alc=ingridient_alc

    def add_ingridient(self):
        """Create new ingridient"""
        parametres_list=[]
        while True:
            new_name=input('Enter new name ')
            new_volume=input('Enter volume ')
            new_price=input('Enter price  ')
            new_alc=input('Enter alchoholdegree  ')
            if Utilities.check_digit(new_volume or new_price or new_alc)==False:
                        break
            parametres_list.append(new_name,new_volume,new_price,new_alc)
            break
        return parametres_list
     
class NoAlchohol(Ingridient):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(self)
        self.ingridient_name=ingridient_name
        self.ingridient_volume=ingridient_volume
        self.ingridient_price=ingridient_price

    def add_ingridient(self):

        parametres_list=[]
        while True:
            new_name=input('Enter new name ')
            new_volume=input('Enter volume ')
            new_price=input('Enter price  ')
            if Utilities.check_digit(new_volume or new_price)==False:
                        break
            parametres_list.append(new_name,new_volume,new_price)
            break
        return parametres_list
       
class HotDrink(Alchohol):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price,ingridient_alc):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price,ingridient_alc)
       
    def add_hotdrink(self):
        """ 'ingr' means ingridient"""
        param_list = self.add_ingridient()
        return HotDrink(param_list[0], param_list[1], param_list[2], param_list[3])
    
class Liquor(Alchohol):

    def __init__(self,ingridient_name,ingridient_volume,ingridient_price,ingridient_alc):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price,ingridient_alc)

    def add_liquor(self):
        """ 'ingr' means ingridient"""
        param_list = self.add_ingridient()
        return Liquor (param_list[0], param_list[1], param_list[2], param_list[3])

class Juce(NoAlchohol):
    
    def __init__(self,ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price)

    def add_juce(self):
        """ 'ingr' means ingridient"""
        param_list=self.add_ingridient()
        return Juce(param_list[0], param_list[1], param_list[2])

class Soda(NoAlchohol):
    
    def __init__(self,ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price)

    def add_soda(self):
        """ 'ingr' means ingridient"""
        param_list=self.add_ingridient()
        return Soda(param_list[0], param_list[1], param_list[2])

class Syrop(NoAlchohol):

    def __init__(self,ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price)

    def add_syrop(self):
        """ 'ingr' means ingridient"""
        param_list=self.add_ingridient()
        return Syrop(param_list[0], param_list[1], param_list[2])
