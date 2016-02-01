#!/usr/bin/python

# A very simple script for generating rust headers for extern "C" from C headers
#
# Usage:
#        ./gernerate data.c
#
# This will create data.rs which you can then copy and paste into the extern "C"
# portion of code. The next step in porting the library is making it safe by
# writing a rust wrapper that puts the C Function in an unsafe { block }.

import sys

export = ''
code = None
c_file = sys.argv[1]
with open(c_file) as f:
    code = f.readlines()
for line in code:
    line = line.replace("SB_API ", "")
    line = line.replace("S_CALLTYPE ", "")
    line = line.replace(";", " -> ")
    line = line.replace("\n", "")
    line = line.replace("uint16", "u16")
    line = line.replace("uint32", "u32")
    line = line.replace("int", "c_int")
    function_index = line.find('I')
    if function_index != -1:
        line = line[function_index:] + line[:function_index-1] + ";\n"
    line = "fn " + line
    export = str(export) + line
out = open(c_file[:-1] + "rs", "w")
out.write(export)
