import sys,random,string
import logging
from ShakerInterface import IInterface


class Utilities:
    
    def check_len(self,input_data):

        if len(input_data)>2:
            raise "Wrong input data"
        else:
            pass

    def check_digit(self,input_data=''):
        
        if input_data.replace('.','',1).isdigit()==True:
            return True
        else:
            print("Warning: wrong enter!")
            return False

    def random_name(self):
        random_name=''
        l1=random.randrange(65,90,1)
        lit=string.ascii_lowercase
        random_name=chr(l1)+''.join(random.choice(lit) for _ in range(1,9))
        return random_name


class CSVReader(IInterface):

    def read(self, file_name):
        """Read from .csv file"""

        import csv
        csv_data=[]  
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count==0:
                    line_count+=1
                else:
                    csv_data.append([row[0]]+[row[1:]])  #gives us array list
                    line_count+=1
        return csv_data


class XLSReader(IInterface):
    
    def read(self,file_name):
        """Read from .xls file"""

        import xlrd, xlwt
        readbook = xlrd.open_workbook(file_name,formatting_info=True)
        sheet = readbook.sheet_by_index(0)
        xls_data = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
        return xls_data

class PickleReader(IInterface):

    def read(self,file_name):
        """Read from .pickle file"""

        import pickle
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
        return data

class JsonReader(IInterface):

    def read(self,file_name):
        """Read from .json file"""

        import json
        with open(sys.argv[1], 'r') as f:
            data=json.load(f)
            logging.info("Read done!")
        return data

class ReadersFactory(IInterface):
    """ 
    Can choose Reader for file;
    :param file_name: include file location and file name
    :return: array of coordinates from file
    """   
    def read(self,file_name):
        import pathlib
        readers_dict={ '.csv': CSVReader()
                      ,'.xls': XLSReader()
                      ,'.pickle': PickleReader()
                      ,'.json': JsonReader()
                      }
        file_extension=pathlib.Path(file_name).suffix
        for i,j in readers_dict.items():
            if i==file_extension:
                file_data=j.read(file_name)
        return file_data


