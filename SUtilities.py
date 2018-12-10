import sys,random, string
import xlrd, xlwt
from ShakerInterface import *
from SIngridient import *
from SCoctails import *

def check_len(input_data):

    if len(input_data)>2:
        raise "Wrong input data"
    else:
        pass

def check_digit(input_data=''):
    
    if input_data.replace('.','',1).isdigit()==True:
        return True
    else:
        print("Warning: wrong enter!")
        return False

def random_name():
    random_name=''
    l1=random.randrange(65,90,1)
    lit=string.ascii_lowercase
    random_name=chr(l1)+''.join(random.choice(lit) for _ in range(1,9))
    return random_name

def read_xlsfile(filename):
    """Used excel files"""
    rb = xlrd.open_workbook(filename,formatting_info=True)
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    return vals