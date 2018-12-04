from ShakerInterface import IShaker
from SIngridient import *
import pickle,sys
from SUtilities import *


class Coctail(IShaker):

    def __init__(self,coctail_name,args=[]):
        IShaker.__init__(self)
        self.coctail_name=coctail_name
        self.args=args
    
    def add(self,file_name,add_data):
        with open(file_name, 'wb') as f:
            pickle.dump(add_data,f)
    
    def read(self,file_name):
        with open (file_name, 'rb') as f:
            data_new=pickle.load(f)
        return data_new
    
    def show(self,data):
        print(data)

    def add_coctail(self):             
        """Add new coctail"""
        ai=input('Enter new coctail name ')
        ingridient_dict=Ingridient.read(self,'Ingridients.pickle')
        for i,j in ingridient_dict.items():
            print(i+ ' '+ j.ingridient_name)
        ap=[]
        while True:
            z=input('Enter № of ingridients or stop')
            if z=='stop':
                break
            else:
                check_digit(z)
                ap.append(z)
        return Coctail(ai,ap)

    def price_calculation(self):
        pass
    
    def volume_calculation(self):
        pass

    def alc_calculation(self):
        pass
        
    def edit_coctail(self):
        pass
