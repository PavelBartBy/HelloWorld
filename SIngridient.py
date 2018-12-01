from ShakerInterface import IShaker


class Ingridient(IShaker):

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

    def add_ingridient(self):
        #add ingridient to menu
        pass

    def edit_ingridient(self):
        #edit ingridient
        pass

class Alchohol(Ingridient):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price,ingridient_alc):
        super(Alchohol,self).__init__(self)
        self.ingridient_name=ingridient_name
        self.ingridient_volume=ingridient_volume
        self.ingridient_price=ingridient_price
        self.ingridient_alc=ingridient_alc

    def add_part(self):                          #перенести в класс создающий файл с меню!!!
        
        ai=input('Enter new ingridient name ')
        av=input('Enter volume of ingridient ')
        ap=input('Enter price of ingridient ')
        ad=input('Enter alchoholdegree of ingridient ')
        return Alchohol(ai,av,ap,ad)
           
    
class NoAlchohol(Ingridient):

    def __init__(self, ingridient_name,ingridient_volume,ingridient_price):
        super(NoAlchohol,self).__init__(self)
        self.ingridient_name=ingridient_name
        self.ingridient_volume=ingridient_volume
        self.ingridient_price=ingridient_price
        
class HotDrink(Alchohol):
    
    def __init__(self):
        super(HotDrink,self).__init__(self)

        def add_part(self):                             #перенести в класс где создантся меню
            ai=input('Enter new ingridient name ')
            av=input('Enter volume of ingridient ')
            ap=input('Enter price of ingridient ')
            ad=input('Enter alchoholdegree of ingridient ')
            pass

class Liquor(Alchohol):

    def __init__(self):
        super(Liquor,self).__init__(self)

class Juce(NoAlchohol):
    
    def __init__(self):
        super(Juce, self).__init__(self)

class Soda(NoAlchohol):
    
    def __init__(self):
        super(Soda,self).__init__(self)

class Syrop(NoAlchohol):

    def __init__(self):
        super(Syrop,self).__init__(self)
