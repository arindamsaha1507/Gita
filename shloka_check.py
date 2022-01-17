import pandas as pd
from read_shloka import create_list

def remove_linebreaks(s):

    start = 0
    for i in range(4):
        pos = s.find('\n', start)
        print(pos)
        if pos > 0:
            if s[pos-1] != '॥' and s[pos-1] != '।':
                s = s[:pos] + s[pos+1:]
            else:
                start = pos+1

    return(s)

if __name__ == '__main__':

    ss = create_list()

    # print(ss)

    ff = open('test.txt', 'w')

    for ii in range(len(ss)):

        jj = ss[ii].index('॥')

        ss[ii] = ss[ii][:jj+1] + '\n'

        ss[ii] = remove_linebreaks(ss[ii])

        ss[ii] = ss[ii] + '\n'

        ff.write(ss[ii])

    ff.close()