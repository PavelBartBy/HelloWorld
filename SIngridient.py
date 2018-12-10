from ShakerInterface import IShaker,IInterface
import pickle
#from SUtilities import *


class Ingridient(IShaker,IInterface):

    def __init__(self,*args, **kwargs):
        IShaker.__init__(self)
        IInterface.__init__(self)
    
    def write(self):
        pass
    
    def add(self,file_name,add_data):
        with open(file_name, 'wb') as f:
            pickle.dump(add_data,f)
    
    def read(self,file_name):
        with open (file_name, 'rb') as f:
            data_new=pickle.load(f)
        return data_new
    
    def show(self,file_name):
        ingridient_dict=Ingridient.read(self,file_name)
        for i,j in ingridient_dict.items(): 
            print(i+ ' '+ j.ingridient_name)
    
    def check_ingridienttype(self,ingr):
        """Check that add Alchohol or NoAlchohok ingridient"""
        if Alchohol in ingr.__bases__:
            return True
        else:
            return False

    def add_ingridient(self,check_ingridienttype):

        """Create new ingridient"""
        if check_ingridienttype==True:
            while True:
                while True:
                    ai=input('Enter new ingridient name ')
                    av=input('Enter volume of ingridient ')
                    if check_digit(av)==False:
                        break
                    ap=input('Enter price of ingridient ')
                    if check_digit(ap)==False:
                        break
                    ad=input('Enter alchoholdegree of ingridient ')
                    if check_digit(ad)==False:
                        break
                    break
                break
            return ai,av,ap,ad
        else:
            while True:
                while True:
                    ai=input('Enter new ingridient name ')
                    av=input('Enter volume of ingridient ')
                    if check_digit(av)==False:
                        break
                    ap=input('Enter price of ingridient ')
                    if check_digit(ap)==False:
                        break
                    break
                break
            return ai,av,ap 
    
    def edit_ingridient(self):
        """Cant to realize now"""

class Alchohol(Ingridient):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price,ingridient_alc):
        super().__init__(self)
        self.ingridient_name=ingridient_name
        self.ingridient_volume=ingridient_volume
        self.ingridient_price=ingridient_price
        self.ingridient_alc=ingridient_alc

    def get_name(self):
        return self.ingridient_name

    def get_volume(self):
        return self.ingridient_volume

    def get_price(self):
        return self.ingridient_price

    def get_alc(self):
        return self.ingridient_alc

class NoAlchohol(Ingridient):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(self)
        self.ingridient_name=ingridient_name
        self.ingridient_volume=ingridient_volume
        self.ingridient_price=ingridient_price
    
    def get_name(self):
        return self.ingridient_name
    
    def get_name(self):
        return self.ingridient_name

    def get_volume(self):
        return self.ingridient_volume

    def get_price(self):
        return self.ingridient_price
       
class HotDrink(Alchohol):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price,ingridient_alc):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price,ingridient_alc)
       
    def add_hotdrink(self):
        my_ai, my_iv, my_ap, my_ad = Ingridient.add_ingridient(self,True)
        return HotDrink(my_ai,my_iv,my_ap,my_ad)
    
class Liquor(Alchohol):

    def __init__(self,ingridient_name,ingridient_volume,ingridient_price,ingridient_alc):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price,ingridient_alc)

    def add_liqour(self):
        my_ai, my_iv, my_ap, my_ad = Ingridient.add_ingridient(self,True)
        return Liquor (my_ai, my_iv, my_ap, my_ad)

class Juce(NoAlchohol):
    
    def __init__(self,ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price)

    def add_juce(self):
        my_ai, my_iv, my_ap=Ingridient.add_ingridient(self,False)
        return Juce(my_ai, my_iv, my_ap)

class Soda(NoAlchohol):
    
    def __init__(self,ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price)

    def add_soda(self):
        my_ai, my_iv, my_ap=Ingridient.add_ingridient(self,False)
        return Soda(my_ai, my_iv, my_ap)

class Syrop(NoAlchohol):

    def __init__(self,ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(ingridient_name,ingridient_volume,ingridient_price)

    def add_syrop(self):
        my_ai, my_iv, my_ap=Ingridient.add_ingridient(self,False)
        return Syrop(my_ai, my_iv, my_ap)
