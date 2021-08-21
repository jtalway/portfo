def openfile(f):
# File Read Function
    with open(f +'.txt') as fp:
        f_array = []
        f_array = fp.readlines()
        fp.close()
        # print(f_array)
        return(f_array)
