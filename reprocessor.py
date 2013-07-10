import re

# reobj = re.compile(regex)
# result = reobj.sub(newstring, subject)
# re.sub(regex, newstring, subject)

_ReContainer = []

def AddRe(rulefrom, ruleto):
    _ReContainer.append((re.compile(rulefrom), ruleto))

def ClearRe:
    _ReContainer = []

def Process(reobj, data):
    result = data
    for reobj, tostr in _ReContainer:
        result = reobj.sub(tostr, result)
    return result

def ProcessFile(reobj, infile, outfile):
    pass

def ProcessDir(reobj, indir, outdir):
    pass
