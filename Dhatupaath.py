fname = '../Gita/धातुपाठ.md'

with open(fname, 'r') as ff:

    s = ff.readlines()

print(s)

for ll in s:

    if ll[0:2] in ['१.']:
        print(ll)