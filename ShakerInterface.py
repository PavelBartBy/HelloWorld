class IInterface(object):
    def show(self):
        """ Show some data """

    def read(self,file_name):
        """ Read some data"""
    
    def write(self,file_name):
        """Wtite some data"""

    def add(self,*args):
        """Add some data to file"""
  
class IShaker(object):
            
    def add_ingridient(self):
        """Add Ingridient to the Menu"""

    def edit_ingridient(self):
        """Edit Ingridient in the Menu"""

    def create_coctail(self):
        """Create mix of ingridients"""
    
    def add_coctail(self):
        """Add Coctail to the Menu"""
    
    def edit_coctail(self):
        """Edit Coctail in the Menu"""
    
    def get_name(self):
        """Get name of some drink"""

    def get_volume(self):
        """Get some volume of some drink"""
    
    def get_price(self):
        """ Get some price of some drink"""
    
    def get_alc(self):
        """Get alchohol degree of some drink"""
    