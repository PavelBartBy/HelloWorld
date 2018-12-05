import sys,random, string


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

def random_name():
    random_name=''
    l1=random.randrange(65,90,1)
    lit=string.ascii_lowercase
    random_name=chr(l1)+''.join(random.choice(lit) for _ in range(1,9))
    return random_name
