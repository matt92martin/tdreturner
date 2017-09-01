from sys import exit, argv
import re

def make_a_connection(prev, add):
    if len(prev):
        new = prev[:-1] + [ prev[-1] + add[0] ] + add[1:]
    else:
        new = add
    return new

def make_line(line):
    return re.sub(r'[\r\n]*', '', line).split('\t')

def print_line(arr):
    return '\t'.join([re.sub(r'[\r\n]*', '', field) for field in arr])



def fix_file(filename):
    fieldnamesLen = 0
    previous = [ ]
    with open(filename, 'rb') as f:
        for i,line in enumerate(f.readlines()):

            if not i:
                fieldnamesLen = len(make_line(line))

            line = make_line( line )
            if len(line) == fieldnamesLen:

                print print_line(line)

            else:

                previous = make_a_connection( previous, line )
                if len(previous) == fieldnamesLen:

                    print print_line( previous )
                    previous = []

                elif len(previous) > fieldnamesLen:

                    raise Exception("Line is too long!")

                else:

                    continue

if __name__ == '__main__':
    exit(fix_file(argv[1]))