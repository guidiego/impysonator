#!/usr/bin/env python
import sys

from .npl import found_impersonal
from .reader import read

origin = sys.argv[1]
files = read(origin)
imps = []

def main():
    for f in files:
        imps = found_impersonal(f.get_body())

        if len(imps) == 0:
            break

        print('\n\033[91m\033[1m> Arquivo:\033[0m \033[1m{}\033[0m'.format(f.path))

        for i in imps:
            print('  Encontrado \033[1m"{0}"\033[0m na linha \033[1m{1}\033[0m'.format(i["word"], i["line"]))

        print("  \033[93m\033[1mTotal:\033[0m \033[1m{}\033[0m\n".format(len(imps)))

if (__name__ == '__main__'):
    main()