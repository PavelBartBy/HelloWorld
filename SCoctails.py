from ShakerInterface import IShaker
from SIngridient import HotDrink,Liquor,Juce,Soda,Syrop
from SUtilities import Utilities,ReadersFactory
import pickle,sys


class Coctail(IShaker):

    def __init__(self,coctail_name,args=[]):
        super().__init__()
        self.coctail_name=coctail_name
        self.args=args                  #List of ingridient indexes

    def read(self,file_name):
        data_new=ReadersFactory.read(self,file_name)
        return data_new
    
    def show(self,file_name):
        coctil_dict=self.read(file_name)
        for i,j in coctail_dict.items(): 
            print(i+ ' '+ j.coctail_name)
    
    def write(self,data):
        with open('coctails.pickle', 'wb') as f:
            pickle.dump(data, f)

    def add_coctail(self):             
        """Add new coctail"""
        new_coctail=input('Enter new coctail name ')
        self.show('Ingridients.pickle')
        ingridient_list=[]
        while True:
            ingr_number=input('Enter № of ingridients or stop')
            if ingr_number=='stop':
                break
            elif Utilities.check_digit(self,ingr_number)==True:
                ingridient_list.append(ingr_number)
            else:
                break
        return Coctail(coctail_name,ingridient_list)

    def get_price(self):
        ingridient_list=self.args
        ingr=self.read('Ingridient.pickle')
        coctail_price=0
        for i in ingridient_list:
            for w,z in ingr.items():
                if int(i)==int(w):
                    coctail_price+=int(z.ingridient_price)        
        return coctail_price

    def get_volume(self):
        ingridient_list=self.args
        ingr=self.read('Ingridient.pickle')
        for i in ingridient_list:
            for w,z in ingr.items():
                if int(i)==int(w):
                    coctail_volume+=int(z.volume)
        return coctail_volume

    def get_alc(self):
        ingridient_list=self.args
        ingr=self.read('Ingridient.pickle')
        for i in ingridient_list:
            for w,z in ingr.items():
                if int(i)==int(w):
                    coctail_volume+=int(z.volume)
                    if hasattr(z,'alc_degree'):
                        coctail_alc_degree_temp+=float(z.alc_degree)
        coctail_alc_degree=coctail_alc_degree_temp/len(ingridient_list)*coctail_volume/1000
        return coctail_alc_degree

