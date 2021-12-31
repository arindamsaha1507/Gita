def create_list(fname='gita_moola.txt'):

    with open(fname, 'r') as ff:
        lines = ff.readlines()

    start = 0

    shlokas = []

    for i in range(len(lines)):
        if lines[i] == '\n':
            shlokas.append(''.join(lines[start:i]))
            start = i+1

    return shlokas

def get_shloka_number(ch, sh):

    chapter_list = [47, 72, 43, 42, 29, 47, 30, 28, 34, 42, 55, 20, 34, 27, 20, 24, 28, 78]

    ch = ch-1
    sh = sh-1

    if ch < 18 and sh < chapter_list[ch]:
        if ch < 0:
            return sh
        else:
            return sum(chapter_list[:ch]) + sh
    
    else:

        return -1


if __name__ == '__main__':
    print(get_shloka_number(18, 78))