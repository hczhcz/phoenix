_Container = {}
_ContainerByMember = {}
_ContainerByMembers = {}
_MemberToMembers = {}

_AutoFix = True # For uncompleted data
_Finished = False

AcceptedName = frozenset(['[Field]', '[Title]', '[Member]', '[Abstract]', '[Keyword]', ']Award]'])

class Project(object):
    Fair = ''
    ID = ''
    Field = ''
    Title = ''
    Member = None
    Abstract = ''
    Keyword = None
    Award = None

    __Dataset = None
    __FriendlyPrint = None

    def IsTeam(self):
        if _AutoFix and len(self.Member) == 0:
            # self.Member.append('Unknown')
            self.AddData('[Member]', 'Unknown_' + self.Fair + '_' + self.ID)
        assert len(self.Member) > 0
        return len(self.Member) > 1

    def Related(self):
        assert len(self.Member) > 0
        assert set(self.Member) <= _MemberToMembers[self.Member[0]]
        relatedset = _ContainerByMember[self.Member[0]].copy()
        relatedset.discard(self)
        return relatedset

    def IsRelated(self):
        for item in self.Member:
            if _ContainerByMember.has_key(item) and len(_ContainerByMember[item]) > 1:
                return True
        return False

    def IsAwarded(self):
        return len(self.Award) > 0

    def AddData(self, name, value):
        assert not _Finished
        assert name != ''
        assert value != ''

        if name == '[Field]':
            if _AutoFix and len(self.Field) < len(value):
                self.Field = value
            assert self.Field == '' or self.Field == value
            self.Field = value
        elif name == '[Title]':
            if _AutoFix and len(self.Title) < len(value):
                self.Title = value
            assert self.Title == '' or self.Title == value
            self.Title = value
        elif name == '[Member]':
            if not value in self.Member:
                self.Member.append(value)
                assert len(self.Member) <= 3

                allmember = set(self.Member)
                allproject = set([self])
                # Can be optimized if necessary, just iterate last member's data
                for item in self.Member:
                    if _MemberToMembers.has_key(item):
                        cbmkey = min(_MemberToMembers[item])
                        allmember |= _MemberToMembers[item]
                        if _ContainerByMembers.has_key(cbmkey):
                            allproject |= _ContainerByMembers[cbmkey]
                            del _ContainerByMembers[cbmkey]
                for item in allmember:
                    _MemberToMembers[item] = allmember
                    _ContainerByMember[item] = allproject
                _ContainerByMembers[min(allmember)] = allproject
        elif name == '[Abstract]':
            if _AutoFix and len(self.Abstract) < len(value):
                self.Abstract = value
            assert self.Abstract == '' or self.Abstract == value
            self.Abstract = value
        elif name == '[Keyword]':
            if not value in self.Keyword:
                self.Keyword.append(value)
        elif name == '[Award]':
            if not value in self.Award:
                self.Award.append(value)

    def Dataset(self):
        if not _Finished or self.__Dataset == None:
            self.__Dataset = {
                'Fair': self.Fair,
                'ID': self.ID,
                'Field': self.Field,
                'Title': self.Title,
                'IsTeam': self.IsTeam(),
                'Member': self.Member,
                'Abstract': self.Abstract,
                'Keyword': self.Keyword,
                'IsAwarded': self.IsAwarded(),
                'Related': {(item.Fair, item.ID) for item in self.Related()},
                'Award': self.Award,
            }
        return self.__Dataset

    def FriendlyPrint(self):
        if not _Finished or self.__FriendlyPrint == None:
            self.__FriendlyPrint = '[Fair+ID]   ' + self.Fair + ' ' + self.ID + '\n'\
                                + ('[Field]     ' + self.Field + '\n' if self.Field != '' else '')\
                                + ('[Title]     ' + self.Title + '\n' if self.Title != '' else '')\
                                + ('[Author]    ' + self.Member[0] + '\n' if not self.IsTeam() else '[Team]      ' + ', '.join(self.Member) + '\n')\
                                + ('[Abstract]  ' + '\n' + self.Abstract + '\n' if self.Abstract != '' else '')\
                                + ('[Keyword]   ' + ', '.join(self.Keyword) + '\n' if len(self.Keyword) > 0 else '')\
                                + ('[Related]   ' + ', '.join([item.Fair + ' ' + item.ID for item in self.Related()]) + '\n' if self.IsRelated() > 0 else '')\
                                + ('[Award]     ' + '\n' + '\n'.join(self.Award) + '\n' if self.IsAwarded() else '')
        return self.__FriendlyPrint

    def __init__(self, fair, id):
        self.Member = list()
        self.Keyword = list()
        self.Award = list()
        self.Fair = fair
        self.ID = id

    # def __str__(self):
    #     return str(self.Dataset)

    # def __repr__(self):
    #     return repr(self.Dataset)

def GetContainerItem(fair, id):
    assert fair != ''
    assert id != ''
    if not _Container.has_key((fair, id)):
        assert not _Finished
        _Container[(fair, id)] = Project(fair, id)
    return _Container[(fair, id)]

def GetContainer():
    assert _Finished or _AutoFix
    return _Container

def GetMemberContainer():
    assert _Finished or _AutoFix
    return _ContainerByMember

def GetMembersContainer():
    assert _Finished or _AutoFix
    return _ContainerByMembers

def Finish():
    _Finished = True
