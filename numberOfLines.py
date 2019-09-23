import os
rootdir = os.path.dirname(os.path.realpath(__file__))

def file_len(fname):
    with open(fname, 'r', encoding='utf8', errors='ignore') as f:
        i = 0
        for i, l in enumerate(f):
            pass
    return i + 1


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        print (filepath)
        print(file_len(filepath))