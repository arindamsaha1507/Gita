import pandas as pd
from read_shloka import create_list


n_shloka = 414

ff = open('pada_table.csv', 'w')

ss = 'श्लोक,'

ll = ['पद ' + str(x+1) for x in range(25)]
ss = ss + ','.join(ll)

ff.write(ss+'\n')

l = 0
for jj in range(n_shloka):

    df = pd.read_csv('pada.csv')
    ll = list(df['पदाः'])
    mm = ll[jj][1:-1].split(', ')

    for ii in range(len(mm)):
        mm[ii] = mm[ii][1:-1]
        if mm[ii] == '':
            del mm[ii]

    s = ','.join(mm)

    s = str(jj+1) + ',' + s

    ff.write(s+'\n')

    print(s)

print(ss)

ff.close()

########################################################################

ff = open('pada_table.md', 'w')

ff.write('# पद-कोष्टक\n\n')

ss = '| श्लोक | '
ll = ['पद ' + str(x+1) for x in range(25)]
ss = ss + ' | '.join(ll)
ff.write(ss+' |\n')

ss = '| '
ll = ['------' for x in range(25)]
ss = ss + ' | '.join(ll)
ff.write(ss+' |\n')

l = 0
for jj in range(n_shloka):

    df = pd.read_csv('pada.csv')
    ll = list(df['पदाः'])
    mm = ll[jj][1:-1].split(', ')

    for ii in range(len(mm)):
        mm[ii] = mm[ii][1:-1]
        if mm[ii] == '':
            del mm[ii]

    del mm[-1]
    ii = mm.index('।')
    del mm[ii]

    mm = [str('[[') + x + str(']]') for x in mm]

    s = ' | '.join(mm)

    s = '| ' + str(jj+1) + ' | ' + s

    ff.write(s+' |\n')

    print(s)

print(ss)

ff.close()

################################################################################

df = pd.read_csv('pada.csv')
shlokas = create_list()
ll = list(df['पदाः'])

for jj in range(n_shloka):

    mm = ll[jj][1:-1].split(', ')

    fin = 'Sandhi/sandhi_summary_' + str(jj+1) + '.csv'
    fout = 'Obsidian/श्लोक_' + str(jj+1) + '.md'

    ff = open(fout, 'w')

    ff.write('# श्लोक ' + str(jj+1) + '\n\n')

    ff.write(shlokas[jj])

    ff.write('\n\n## पद \n\n')

    for ii in range(len(mm)):
        mm[ii] = mm[ii][1:-1]

        if mm[ii] not in ['।', '॥']:
            ff.write('- [[' + mm[ii] + ']]\n')

    ff.write('\n## सन्धि\n\n')

    with open(fin, 'r') as gg:
        w = gg.readlines()
    
    for kk in range(len(w)):

        cc = w[kk][:-1]
        qq = cc.index('-')
        cc = cc[:qq] + cc[qq+1:]
        ff.write('| ' + ' | '.join(cc.split(',')) + ' |\n')
        if kk == 0:
            ff.write('| ----- | ----- | ----- |\n')

    ff.write('\n\n---\n\n#श्लोक')

    print(w)



    # w = gg.readline()
    # ww = w[:-1].split(',')
    # print(ww)

    ff.close()

# print(shlokas)

#################################################################

df = pd.read_csv('pada.csv')
shlokas = create_list()
ll = list(df['पदाः'])

nn = []

for jj in range(n_shloka):

    mm = ll[jj][1:-1].split(', ')

    for ii in range(len(mm)):
        mm[ii] = mm[ii][1:-1]

        if mm[ii] not in ['।', '॥']:
            nn.append(mm[ii])

print(list(dict.fromkeys(nn)))

print(len(nn))

print(len(set(nn)))