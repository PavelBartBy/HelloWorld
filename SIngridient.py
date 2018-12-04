from ShakerInterface import IShaker,IAdd,IRead,IWrite
import pickle


class Ingridient(IShaker):

    def __init__(self,*args, **kwargs):
        IShaker.__init__(self)
    
    def add(self,file_name,add_data):
        with open(file_name, 'wb') as f:
            pickle.dump(add_data,f)
    
    def read(self,file_name):
        with open (file_name, 'rb') as f:
            data_new=pickle.load(f)
        return data_new

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
        pass

class Alchohol(Ingridient):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price,ingridient_alc):
        super().__init__(self)

class NoAlchohol(Ingridient):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price):
        super().__init__(self)
       
class HotDrink(Alchohol):

    def __init__(self,*args):
        Alchohol.__init__(self)
       
    def add_hotdrink(self):
        return HotDrink(Ingridient.add_ingridient(self,True))

class Liquor(Alchohol):

    def __init__(self,*args):
        super().__init__(self)
    def add_liqour(self):
        return Liquor (Ingridient.add_ingridient(Liquor,True))

class Juce(NoAlchohol):
    
    def __init__(self,*args):
        NoAlchohol.__init__(self)
    def add_juce(self):
        return Juce(Ingridient.add_ingridient(self,False))

class Soda(NoAlchohol):
    
    def __init__(self):
        NoAlchohol.__init__()
    def add_juce(self):
        return Soda(Ingridient.add_ingridient(self,False))

class Syrop(NoAlchohol):

    def __init__(self):
        NoAlchohol.__init__()
    def add_syrop(self):
        return Syrop(Ingridient.add_ingridient(self,False))
