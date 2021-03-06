from random import randrange

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

def nth_root(square, n):
    return square ** (1/n)

def ree():
    return "r" + ("e" * randrange(1,100))

def random_oper(min=0,max=100):
    x = randrange(min,max)
    y = randrange(min,max)
    opers = ['+','-','*','/','**']
    oper = randrange(len(opers))
    return eval ('{}{}{}'.format(x,opers[oper],y))

class rand:
    def __add__ (self, other):
        return random_oper()
    def __sub__ (self,other):
        return random_oper()
    def __mul__ (self,other):
        return random_oper()
    def __div__ (self,other):
        return random_oper()
    def __truediv__ (self,other):
        return random_oper()
    def __mod__ (self,other):
        return random_oper()
    def __pow__ (self,other):
        return random_oper()

    def __lt__ (self,other):
        return True;
    def __gt__ (self,other):
        return True
    def __gt__ (self,other):
        return True
    def __eq__ (self,other):
        return True
    def __ne__ (self,other):
        return True
    def __le__ (self,other):
        return True
    def __ge__ (self,other):
        return True

    def __str__(self):
        return 'True'
    def __int__(self):
        return 1
    def __float__(self):
        return 1.0

    def __repr__ (self):
        return 'True'
    def __hash__(self):
        return 1
    def __len__(self):
        return 0
