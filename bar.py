from utilities import Utilities, ReadersFactory
from cocktails import Cocktail
from ingredients import HotDrink, Liquor, Juice, Soda


class Bar:

    @staticmethod
    def get_cash():
        x = input("Enter your amount of cash ") 
        if Utilities.check_digit(x) == True:
            return x

    def calculate_recommend(self, cash=0):
        print("You can take: ")
        cocktail_data = Cocktail.read(self, 'Cocktails.json')
        for i in cocktail_data:
            if i.get_price() <= cash:
                print(i.coctail_name)

    def ingr_menu(self):
        data = ReadersFactory.read(self,"ingredients_data.json")
        ingr_dict = {'hotdrink': HotDrink(),
                     'liquor': Liquor(),
                     'juice': Juice(),
                     'soda': Soda()}
        ingredients=[]
        for k, v in data['ingredient'].items():
            for x in ingr_dict.keys():
                if k == x:
                    for w,z in v.items():
                        if 'alc_degree' in z.keys():
                            ingredients.append(ingr_dict[x].__init__(w, z['volume'], z['price'], z['alc_degree']))

                        else:
                            ingredients.append(ingr_dict[x].__init__(w, z['volume'], z['price']))
                            print(ingr_dict[x])
        return ingredients

    def create_cocktail(self):

        new_cocktail = Cocktail.add_cocktail(self)
        print('Your coctail: %s  With price: %s Volume: %s And alcohol degree: %s'
              % (new_cocktail.coctail_name, str(Cocktail.get_price(self, new_cocktail)),
                 str(Cocktail.get_alc(self, new_cocktail))))


new_bar = Bar()
print(new_bar.ingr_menu())

# End
