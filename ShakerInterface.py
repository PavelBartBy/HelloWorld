class IInterface(object):
    def show(self):
        """ Show some data """

    def read(self,file_name):
        """ Read some data"""
    
    def write(self,file_name):
        """Wtite some data"""

    def add(self,*args):
        """Add some data to file"""

    def edit(self,*args):
        """Edit some data"""

class IShaker(IInterface):
            
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