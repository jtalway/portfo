from os import lseek
import random

# local filepath
#filepath = './static/assets/'
# remote filepath
filepath = "/home/jtalway/portfo/static/assets/"

def openfile(f):
# File Read Function
    # filepath + filename
    with open(filepath + f +'.txt') as fp:
        f_array = []
        f_array = fp.readlines()
        fp.close()
        # print(f_array)
        return(f_array)


def randomchoice(f):
    with open(filepath + f + '.txt') as fp:
        res = random.choice(list(fp)).rstrip()
        return(res)