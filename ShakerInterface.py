class IShow:
    def show(self):
        """ Show some data """

class IRead:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def read(self,file_name):
        with open(file_name, 'rt') as f:                
            read_file = file_name.read(f)
        return read_file

class IWrite(IInterface):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def write(self,file_name,write_data):
        with open(file_name, 'wt') as f:
            f.write(write_data)

class IAdd(IInterface):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def add(self,file_name,add_data):
        with open(file_name, 'at') as f:
            f.write(add_data)


class IShaker(object):

    def add_ingridient(self):
        pass

    def edit_ingridient(self):
        pass

    def shake_mix(self):
        pass