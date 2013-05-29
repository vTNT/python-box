#!/usr/bin/env python
# -*- coding:utf-8 -*-
 #!/usr/bin/python
# Filename: cat.py

import sys

def readfile(filename):
    '''Print a file to the standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line, # notice comma
    f.close()

# Script starts from here
if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()

if sys.argv[1].startswith('--'):
    print sys.argv
    print sys.argv[1]
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print 'Version 1.2'
    elif option == 'help':
        print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
  --version : Prints the version number
  --help    : Display this help'''
    else:
        print 'Unknown option.'
    sys.exit()
else:
    print sys.argv
    print sys.argv[1:]
    for filename in sys.argv[1:]:
        readfile(filename) 
