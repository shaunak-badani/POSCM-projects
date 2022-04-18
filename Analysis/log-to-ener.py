#! python
"""
Extracts energy entries from a NAMD log file.
Ajasja Ljubetic (@gmail.com).
"""

#import pandas as pd
#import numpy as np
#command line arguments handling 
import argparse 

parser = argparse.ArgumentParser(description='Extracts energy entries from a NAMD log file.',
                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-i','--in-file', 
          help='input file name.', 
          default='namd.log', type=str)
parser.add_argument('-o','--out-file', 
          help='Output file name. Default is same basename as input but with enr extension.', 
          default=None, type=str)

a = parser.parse_args()

if a.out_file is None:
    base = a.in_file.rsplit('.', 1)[0]
    a.out_file = base+'.enr'

print "Converting {} into {}".format(a.in_file, a.out_file)

import subprocess 

#TODO: Could be implemented in pure python

cmd_line = "grep '^ETITLE:' {in_file} | head -n 1 > {out_file}  "\
           .format(in_file=a.in_file, out_file=a.out_file)
print cmd_line
subprocess.call(cmd_line, shell=True)

cmd_line = "grep '^ENERGY:  ' {in_file} >> {out_file}  "\
           .format(in_file=a.in_file, out_file=a.out_file)      
print cmd_line
subprocess.call(cmd_line, shell=True)




