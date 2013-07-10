import os
import re

# reobj = re.compile(regex)
# result = reobj.sub(newstring, subject)
# re.sub(regex, newstring, subject)

_ReContainer = []

def AddRe(rulefrom, ruleto):
    _ReContainer.append((re.compile(rulefrom), ruleto))

def ClearRe():
    _ReContainer = []

def Process(data):
    result = data
    for reobj, tostr in _ReContainer:
        result = reobj.sub(tostr, result)
    return result

def ProcessFile(infile, outfile):
    inhandle = open(infile)
    outhandle = open(outfile, 'w+')
    outhandle.write(Process(inhandle.read()))
    inhandle.close()
    outhandle.close()

def ProcessDir(indir, outdir):
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    for root, subdir, subfile in os.walk(indir):
        for item in subfile:
            # Bug !!!
            # Flatten subdirs and cannot handle duplication of name
            # I am lazy xD
            ProcessFile(os.path.join(root, item), os.path.join(outdir, item))
