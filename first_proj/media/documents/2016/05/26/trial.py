import re
import statistics
def read_words(fname):
    with open(fname) as f:
        content=f.readlines()
    words=[]
    for i in content:
        words.append(get_words_from_string(i))
    return words

def get_words_from_string(s):
    return (set(re.findall(r"\w+",s)))

def semordnilap(fname):
    a=read_words(fname)
    b = set()
    for i in a:
        for j in i:
            b.add(j)

