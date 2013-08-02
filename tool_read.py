import container

# Warning !!!
# ByStr() methods of Query() are not secure

class _QueryBase(object):
    _Result = None

    def _StrToLambda(self, str):
        assert False

    def Count(self):
        return len(self._Result)

    def Select(self, func):
        self._Result = {item for item in self._Result if func(item)}

    def SelectByStr(self, str):
        self.Select(self._StrToLambda(str))

    def Iterate(self, func):
        return {func(item) for item in self._Result}

    def IterateByStr(self, str):
        return self.Iterate(self._StrToLambda(str))

    def Eval(self, func, start = 0):
        result = start
        for item in self._Result:
            result += func(item)
        return result

    def EvalByStr(self, str):
        return self.Eval(self._StrToLambda(str))

    def PrintToString(self):
        assert False

    def PrintToFile(self, file):
        handle = open(file, 'w')
        handle.write(self.PrintToString())
        handle.close()

class Query(_QueryBase):
    def _StrToLambda(self, str):
        return lambda dataobj: (lambda data: eval(str))(dataobj.Dataset())

    def PrintToString(self):
        result = ''
        for item in self._Result:
            result += item.FriendlyPrint() + '\n'
        return result

    def __init__(self):
        self._Result = set(container.GetContainer().values())

class MultiQuery(_QueryBase):
    def _StrToLambda(self, str):
        return lambda dataobj: (lambda data, summary: eval(str))([item.Dataset() for item in dataobj], self.Summaryset(dataobj))

    def Summaryset(self, data):
        assert len(data) > 0
        firstone = list(data)[0]
        return {
            'IsAwarded': True in {item.IsAwarded() for item in data},
            'CoveredAward': {subitem for item in data for subitem in item.Award},
            'CoveredMember': {subitem for item in data for subitem in item.Member},
            'MemberChanged': True in {set(item.Member) != set(firstone.Member) for item in data},
            'FieldChanged': True in {item.Field != firstone.Field for item in data}
        }

    def PrintToString(self):
        result = ''
        for item2 in self._Result:
            for item in item2:
                result += item.FriendlyPrint() + '\n'
            result += '============\n\n'
        return result

    def __init__(self, bymember = False):
        if bymember:
            self._Result = {frozenset(item) for item in container.GetMemberContainer().values()}
        else:
            self._Result = {frozenset(item) for item in container.GetMembersContainer().values()}
