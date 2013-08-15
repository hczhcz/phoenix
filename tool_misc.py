def ListToExcel(list):
    result = ''
    for line in list:
        for item in line:
            result += str(item) + '\t'
        result += '\n'
    return result