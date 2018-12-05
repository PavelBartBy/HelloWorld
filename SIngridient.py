from ShakerInterface import IShaker,IInterface
import pickle


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

    def add_ingridient(self,check_ingridienttype):

        if check_ingridienttype==True:
            ai=input('Enter new ingridient name ')
            av=input('Enter volume of ingridient ')
            ap=input('Enter price of ingridient ')
            ad=input('Enter alchoholdegree of ingridient ')
            check_ingridienttype=None
            return ai,av,ap,ad
        else:
            ai=input('Enter new ingridient name ')
            av=input('Enter volume of ingridient ')
            ap=input('Enter price of ingridient ')
            return ai,av,ap 

    def check_ingridienttype(self,ingr):
        """Check that add Alchohol or NoAlchohok ingridient"""
        if Alchohol in ingr.__bases__:
            return True
        else:
            return False
    
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
        super().__init__(self, ingridient_name,ingridient_volume,ingridient_price,ingridient_alc)
       
    def add_hotdrink(self):
        return HotDrink(Ingridient.add_ingridient(self,True))
    

class Liquor(Alchohol):

    def __init__(self,ingridient_name,ingridient_volume,ingridient_price,ingridient_alc):
        super().__init__(self, ingridient_name,ingridient_volume,ingridient_price,ingridient_alc)

    def add_liqour(self):
        return Liquor (Ingridient.add_ingridient(Liquor,True))

class Juce(NoAlchohol):
    
    def __init__(self,ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(self,ingridient_name,ingridient_volume,ingridient_price)

    def add_juce(self):
        return Juce(Ingridient.add_ingridient(self,False))

class Soda(NoAlchohol):
    
    def __init__(self,ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(self,ingridient_name,ingridient_volume,ingridient_price)

    def add_juce(self):
        return Soda(Ingridient.add_ingridient(self,False))

class Syrop(NoAlchohol):

    def __init__(self,ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(self,ingridient_name,ingridient_volume,ingridient_price)

    def add_syrop(self):
        return Syrop(Ingridient.add_ingridient(self,False))
