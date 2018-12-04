class IShow:
    def show(self):
        """ Show some data """

class IRead:
    """ Read some data"""
    def read(self,file_name):
        with open(file_name, 'rt') as f:                
            read_file = file_name.read(f)
        return read_file

class IWrite:
    """Wtite some data"""
    def write(self,file_name,write_data):
        with open(file_name, 'wt') as f:
            f.write(write_data)

class IAdd:
    """Add some data to file"""
  
class IShaker(object):
    
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__
        
    def add_ingridient(self):
        """Add Ingridient to the Menu"""

    def edit_ingridient(self):
        """Edit Ingridient in the Menu"""

    def shake_mix(self):
        """Create mix of ingridients"""
    
    def add_coctail(self):
        """Add Coctail to the Menu"""
    
    def edit_coctail(self):
        """Edit Coctail in the Menu"""