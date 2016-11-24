_store = {}
_store['input'] = input
print('MorkPy imported. https://github.com/MorkHub/MorkPy')
def input (prompt='Input a number: ',type=int,error='Error - Wrong Type',ascii=False):
    temp = None
    while temp is None:
        temp = _store['input'](str(prompt))
        try:
            temp = type(temp)
        except ValueError:        
            if ascii:
                return ord(temp[0])
            else:
                temp = None
                continue
    return temp
