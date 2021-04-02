
import sys
from os import listdir
from os.path import isfile, join

exts=set()
uniq=set()

def idx(st,sb):
    try:
        return st.index(sb)
    except ValueError:
        return -1

def get_extension(fname):
    fname=fname.split('.')
    if idx(fname[-1],'\\')!=-1 or idx(fname[-1],'/')!=-1:
        fname=''
    return fname[-1]

def search_here(fname):
    for f in listdir(fname):
        if isfile(join(fname,f)):
            ext=get_extension(join(fname,f))
            if ext not in exts:
                uniq.add(ext)
            elif ext in uniq:
                uniq.remove(ext)
            exts.add(ext)
        else:
            search_here(join(fname,f))

if len(sys.argv)!=2:
    print('pass path to arguments')
    exit()
path=sys.argv[1]
search_here(path)
print('Number of different extensions: ',len(exts))
print('Unique extensions: ',", ".join(map(str,uniq)))
