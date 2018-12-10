from SIngridient import HotDrink,Liquor,Juce,Soda,Syrop,Ingridient
from SCoctails import Coctail


class Menu(HotDrink,Liquor,Juce,Soda,Syrop):

    def __init__(self):
        Ingridient.__init__(self)
       
    def ingridients_to_file(self):
            ingridient_dict={}
            j=0
            while True:
                x=input("Choose type of ingridient: HotDrink, Liqour, Juce, Soda, Syrop  or stop ") 
                if x=="HotDrink":
                    ingridient_dict[j]=HotDrink.add_hotdrink(self)
                    print('Done')
                elif x=="Liqour":
                    ingridient_dict[j]=Liquor.add_liqour(self)
                elif x=="Juce":
                    ingridient_dict[j]=Juce.add_juce(self)
                elif x=="Soda":
                    ingridient_dict[j]=Soda.add_soda(self)
                elif x=="Syrop":
                    ingridient_dict[j]=Syrop.add_syrop(self)
                elif x=="stop":
                    break
                j+=1
            Ingridient.add(self,'Ingridients.pickle',ingridient_dict)
    
    def coctails_to_file(self):
        coctails_list=[]
        while True:
            x=input('Add new coctail? yes/no ')
            if x=='yes':
                coctails_list.append(Coctail.add_coctail(self))
            if x=='no':
                break
        Coctail.add(self,'Coctails.pickle', coctails_list)

    def ingridients_fxls(self,dict):
        ingridients={}
        m=0
        for i in dict[0:5]:   #Parametres for HotDrinks      
            ingridients[m]=HotDrink(i[0:4][0],i[0:4][1],i[0:4][2],i[0:4][3])
            m+=1
        for i in dict[5:9]:
            ingridients[m]=Liquor(i[0:4][0],i[0:4][1],i[0:4][2],i[0:4][3])
            m+=1
        for i in dict[9:12]:
            ingridients[m]=Juce(i[0:3][0],i[0:3][1],i[0:3][2])
            m+=1
        for i in dict[12:15]:
            ingridients[m]=Soda(i[0:3][0],i[0:3][1],i[0:3][2])
            m+=1
        for i in dict[15:18]:
            ingridients[m]=Syrop(i[0:3][0],i[0:3][1],i[0:3][2])
            m+=1
        return ingridients

    def coctails_fxls(self,dict):
        coctails=[]
        for i in range(0,8):
            coctails.append(Coctail(dict[i][0],dict[i][1]))
        return coctails

