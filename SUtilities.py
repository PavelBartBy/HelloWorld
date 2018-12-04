import sys


def check_len(input_data):

    if len(input_data)>2:
        raise "Wrong input data"
    else:
        pass

def check_digit(input_data=''):

    if input_data.replace('.','',1).isdigit()==True:
        pass
    else:
        raise "Wrong input data"