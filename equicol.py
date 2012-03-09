#!/usr/bin/python

# Michael Yu
# mikeyu@ucsd.edu
# 3-8-12

import argparse

def main():
    buff = 2

    parser = argparse.ArgumentParser(description='Replace tab characters in a TSV file with a sufficient number of spaces so that columns are aligned.')
    parser.add_argument('-i', required=True, help='input TSV file')
    parser.add_argument('-o', required=True, help='output space-separated file')
    parser.add_argument('-b', default=buff, type=int, help='Extra space between columns (default: %s)' % buff)
    args = parser.parse_args()
    
    assert args.b >= 1, 'Buffer must be greater than or equal to 1'
    buff = args.b
    
    # Split file into lines
    lines = [x.split() for x in open(args.i).read().split('\n')]
    
    # Number of columns
    num_cols = [len(x) for x in lines if len(x)!=0]
    assert len(set(num_cols))==1, 'Error: Some rows have different number of columns'
    num_cols = num_cols[0]

    # Format empty lines
    lines = [(x if x!=[] else ['' for i in range(num_cols)]) for x in lines]

    # Max width of every column
    max_widths = [max([len(x[i]) for x in lines]) for i in range(len(lines[0]))]

    # Replace tabs with spaces
    lines = [''.join([a.ljust(w + buff) for a, w in zip(line, max_widths)[:-1]]) + (line[-1] if line!=[] else '') for line in lines]

    # Write output
    open(args.o, 'w').write('\n'.join(lines))

if __name__=='__main__':
    main()
