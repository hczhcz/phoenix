# import reprocessor
from reprocessor import *

def InitDatabase():
    AddRe(r'____+___', r'')
    AddRe(r'(\n| |<br>)+\n|\n(\n| |<br>)+', r'\n')
    AddRe(r' +', r' ')
    AddRe(r'(<br>)+', r'<br>')

    AddRe(r'(\d\d\d\d) - ([A-Z][A-Z])(\d\d\d)\n(.+)\n(.+)\n(.+)\n(.+)', r'[Fair]\n\1\n[ID]\n\2\3\n[Field]\n\2\n[Title]\n\4\n[Member]\n\5\n[School]\n\6\n[Abstract]\n\7')
    AddRe(r'Awards won at .*', r'[Award]')

    AddRe(r'\[Member\]\n(.+)[,\&] (.+)', r'[Member]\n\1\n[Member]\n\2')
    AddRe(r'\[Member\]\n(.+)[,\&] (.+)', r'[Member]\n\1\n[Member]\n\2')
    AddRe(r'\[School\]\n(.+)[;\&] (.+)', r'[School]\n\1\n[School]\n\2')
    AddRe(r'\[School\]\n(.+)[;\&] (.+)', r'[School]\n\1\n[School]\n\2')

    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    AddRe(r'\[Award\]\n(.+)\n(?!\[)(.+)', r'[Award]\n\1\n[Award]\n\2')
    ProcessDir('data', 'processeddata')

if __name__ == '__main__':
    InitDatabase()
