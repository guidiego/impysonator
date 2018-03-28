import sys

from npl import found_impersonal
from reader import read

origin = sys.argv[1]
files = read(origin)
imps = []

for f in files:
    imps = found_impersonal(f.get_body())

    if len(imps) > 0:
        print('> File: {}'.format(f.name))

    for i in imps:
        print('  Found "{0}" in line "{1}"'.format(i["word"], i["line"]))