from ShakerInterface import IShaker
from SIngridient import *
import pickle,sys
#from SUtilities import *


class Coctail(IShaker,IInterface):

    def __init__(self,coctail_name,args=[]):
        super().__init__()
        self.coctail_name=coctail_name
        self.args=args                  #List of ingridient indexes
    
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

    def write(self):
        pass

    def add_coctail(self):             
        """Add new coctail"""
        ai=input('Enter new coctail name ')
        Ingridient.show(self,'Ingridients.pickle')
        ap=[]
        while True:
            z=input('Enter № of ingridients or stop')
            if z=='stop':
                break
            else:
                if check_digit(z)==True:
                    ap.append(z)
                else:
                    break
        return Coctail(ai,ap)

    def get_price(self):
        num_this=self.args
        ingr=self.read('Ingridient.pickle')
        coctail_price=0
        for i in num_this:
            for w,z in ingr.items():
                if int(i)==int(w):
                    coctail_price+=int(z.ingridient_price)        
        return coctail_price

    def get_volume(self):
        num_this=some_coctail.args
        ingr=self.read('Ingridient.pickle')
        for i in num_this:
            for w,z in ingr.items():
                if int(i)==int(w):
                    coctail_volume+=int(z.volume)
        return coctail_volume

    def get_alc(self):
        num_this=some_coctail.args
        ingr=self.read('Ingridient.pickle')
        for i in num_this:
            for w,z in ingr.items():
                if int(i)==int(w):
                    coctail_volume+=int(z.volume)
                    if hasattr(z,'alc_degree'):
                        coctail_alc_degree_temp+=float(z.alc_degree)
        coctail_alc_degree=coctail_alc_degree_temp/len(num_this)*coctail_volume/1000
        return coctail_alc_degree

    def get_name(self):
        return self.coctail_name

    def edit_coctail(self):
        """Cant to realize now"""

