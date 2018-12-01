from ShakerInterface import IShaker


class Coctail(IShaker):

    def __init__(self,coctail_name,coctail_volume,coctail_price,coctail_alc):
        super(Coctail,self).__init__(self)
        self.coctail_name=coctail_name
        self.coctail_volume=coctail_volume
        self.coctail_price=coctail_price
        self.coctail_alc=coctail_alc

    def add_ingridient(self):             #перенести в класс где создантся меню
        # add coctail to menu
        ai=input('Enter new coctail name ')
        pass
    
    def edit_ingridient(self):            #перенести в класс где создантся меню
        #edit coctail parametres
        pass
