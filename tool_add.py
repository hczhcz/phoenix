import os
import container

class Session(object):
    __CurrentProject = None
    __CurrentFair = ''

    __PreAssign = None

    def __AddProject(self, id):
        assert self.__CurrentFair != ''
        self.__CurrentProject = container.GetContainerItem(self.__CurrentFair, id)
        for item in self.__PreAssign.items():
            self.__CurrentProject.AddData(item[0], item[1])

    def Add(self, name, value):
        # name = name.strip()
        # value = value.strip()
        if name == '' or value == '':
            pass
        elif name == 'ID':
            self.__AddProject(value)
        elif name == 'Fair':
            self.__CurrentFair = value
        elif name in self.__PreAssign.keys():
            self.__CurrentProject = None
            self.__PreAssign[name] = value
        else:
            self.__CurrentProject.AddData(name, value)

    def __init__(self, fair = '', pre = None):
        if pre == None:
            self.__PreAssign = {'Award': ''}
        else:
            self.__PreAssign = pre
        self.__CurrentFair = fair

def AddList(fair, list, pre = None):
    assert fair != ''

    tosession = Session(fair, pre)
    name = ''
    value = ''

    def Fin(name, value):
        if name != '' or value != '':
            assert name != ''
            assert value != ''
            tosession.Add(name, value)

    for rawline in list:
        line = rawline.strip()
        if line == '':
            pass
        elif line in container.AcceptedName or line == 'ID' or line == 'Fair':
            Fin(name, value)
            name = ''
            value = ''
            name = line
        else:
            if value != '':
                value += '\n'
            value += line

    Fin(name, value)

def AddFile(fair, file, pre = None):
    handle = open(file)
    AddList(fair, handle.readlines(), pre)
    handle.close()

def AddDir(fair, dir, pre = None):
    for root, subdir, subfile in os.walk(dir):
        for item in subfile:
            AddFile(fair, os.path.join(root, item), pre)
