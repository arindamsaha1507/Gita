from varna import *

def get_vinyaasa(shabda):

    vinyaasa = []

    for i in range(len(shabda)):

        # print(shabda[i])
        
        x = shabda[i]
        
        if x in svara:
            vinyaasa.append(x)
        elif x in vyanjana_with_akaara:
            vinyaasa.append(x+'्')
            if i+1 < len(shabda):
                if shabda[i+1] in vyanjana_with_akaara or shabda[i+1] in avasaana or shabda[i+1] in ['ः', 'ं']:
                    vinyaasa.append('अ')
                elif shabda[i+1] in ['ँ']:
                    vinyaasa.append('अँ')
            else:
                vinyaasa.append('अ')

        elif x in maatraa:
            # vinyaasa.append(maatraa_to_svara[x])
            if i+1 < len(shabda):
                if shabda[i+1] in ['ँ']:
                    vinyaasa.append(maatraa_to_svara[x]+'ँ')
                else:
                    vinyaasa.append(maatraa_to_svara[x])
            else:
                vinyaasa.append(maatraa_to_svara[x])
        elif x in ['्', 'ँ']:
            pass
        else:
            vinyaasa.append(x)
    
    return vinyaasa


def get_shabda(vinyaasa):

    shabda = ''

    for ii in range(len(vinyaasa)):

        varna = vinyaasa[ii]

        if ii == 0 and varna in svara:
            jj = varna
        elif varna in svara and (vinyaasa[ii-1] in svara or vinyaasa[ii-1] == ' '):
            jj = varna
        elif varna in vyanjana and ii+1 < len(vinyaasa):
            if vinyaasa[ii+1] in svara or vinyaasa[ii+1] in anunaasika_svara:
                jj = varna[0]
            else:
                jj = varna
        elif varna == 'अ':
            jj = ''
        elif varna in svara:
            jj = svara_to_maatraa[varna]
        elif varna in anunaasika_svara:
            jj = svara_to_maatraa[varna[0]] + 'ँ'
        else:
            jj = varna

        shabda = shabda+jj

    return shabda


if __name__ == '__main__':

    y = 'समवेतारुँ'
    x = get_vinyaasa(y)
    print(x)
    print(list(ii for ii in y))
    print(get_shabda(x))
