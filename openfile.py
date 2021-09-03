def openfile(f):
# File Read Function
    with open('./static/assets/'+ f +'.txt') as fp:
    #with open('/home/jtalway/portfo/static/assets/'+ f +'.txt') as fp:
        f_array = []
        f_array = fp.readlines()
        fp.close()
        # print(f_array)
        return(f_array)
