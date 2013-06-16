from BeautifulSoup import BeautifulSoup
from datetime import timedelta, datetime

dbg=False

def import_list(data):
    soup = BeautifulSoup(data)

    bs=soup.findAll('font')


    names = []
    for idx,bb in enumerate(bs):
        if len(bb)>20: 
            names.extend(bb.getText(',').split(','))

    print len(names)
    return names


def vowel_count(names):
    vnames = []
    for name in names:
        if len(name)==0: continue
        if name[-1] in vowel_sound or name[-2:] in vowel_sound:
            vnames.append(name)

    print float(len(vnames))/len(names)

vowel_sound = set([ 'a', 'ie', 'o', 'oh', 'ah', 'uh', 'yh' , 'y', 'i', 'u'])
if __name__ == "__main__":
    import sys
    data=open(sys.argv[1]).read()
    names = import_list(data)
    vowel_count(names)
