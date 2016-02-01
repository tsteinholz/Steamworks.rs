#!/usr/bin/python
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
    function_index = line.find('I')
    if function_index != -1:
        line = line[function_index:] + line[:function_index-1] + ";\n"
    line = "fn " + line
    export = str(export) + line
out = open(c_file[:-2] + ".rs", "w")
out.write(export)
