def myfunc(string):
    sarc = []
    for _ in range(len(string)):
        if _%2 == 0:
            sarc.append(string[_].lower())
        else:
            sarc.append(string[_].upper())
    return ''.join(sarc)
