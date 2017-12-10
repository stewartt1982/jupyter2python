#
# A small program to extract source code from Jupyter files
# and output it to a text python .py file
#

import sys
import argparse
import json
from os.path import basename
from os.path import splitext

def main():
    #create and define the command line argument parser
    parser = argparse.ArgumentParser(description='Convert Jupyter JSON file to python .py file')
    parser.add_argument('inputfile',metavar='inputfile',type=str,nargs='+',
                       help='input source file(s)')
    #add this feature later
    #parser.add_argument('--d',help='create new file in the same directory as inputfile')
    args = parser.parse_args()
    print args
    #args.inputfile will have our input files
    for f in args.inputfile:
        #open source, we really should check if it exists but will add later
        fp = open(f,"r")
        #open output file
        base = basename(f)
        ofname = str(splitext(base)[0]) + ".py"
        of = open(ofname,"w")
        readJSON = json.loads(fp.read().decode('utf-8'))
        #check nbformat, two different ways to extract the python source
        if readJSON["nbformat"] >= 4:
            #we want to look at cells or cell_type "code"
            for cell in readJSON["cells"]:
                if str(cell["cell_type"])=="code":
                    for line in cell["source"]:
                        of.write(line.encode('ascii', 'ignore').decode('ascii')+"\n")
        fp.close()
        of.close()
                    
if __name__ == "__main__":
    main()
