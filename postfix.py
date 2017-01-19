bidmas = {'*':3,
          '/':3,
          '+':2,
          '-':2,
          '(':1}
alpha = 'ABCDEFGHIJKLNOPQRSTUVWXYZ0123456789.'

class Stack:
    """python implementation of a stack data structure """
    def __init__(self):
        self.items = []
        self.length = 0
        
    def push(self, val):
        self.items.append(val)
        self.length += 1
        
    def pop(self):
        if self.isempty():
            return None
        self.length -= 1
        return self.items.pop()
        
    def size(self):
        return self.length
    
    def peek(self):
        if self.isempty():
            return None
        return self.items[0]
    
    def isempty(self):
        return self.length == 0
    
    def __str__(self):
        return str(self.items)

def tokenise(infix):
    """Convert infix to tokens for conversion to postfix. Credit goes to Shwam3 for this function"""
    infix = infix.replace(' ','')
    tokens = []
    cur_num = ''
    
    for index,char in enumerate(infix):
        if char in bidmas:
            if cur_num:
                tokens.append(cur_num)
                cur_num = ''
                
            if char == '*' and infix[index+1] == '*' or char == '^':
                tokens.append('**')
            else:
                tokens.append(char)
        else:
            cur_num += char
        
    if cur_num:
        tokens.append(cur_num)
        
    return tokens

def isAlpha(token):
    """Returns True if all chars in token are alphanumerical (with exceptions)"""
    for char in token:
        if not char.upper() in alpha:
            return False
    return True

def toPostfix(tokens):
    """Convert a list of tokens to postfix, for mathematical resolution"""
    opstack = Stack()
    postfix = []
    
    for token in tokens:
        if isAlpha(token.lower()):
            postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            while True:
                tmp = opstack.pop()
                if tmp == None or tmp == '(':
                    break
                elif not isAlpha(tmp.lower()):
                    postfix.append(tmp)
        else:
            if not opstack.isempty():
                tmp = opstack.peek()
                while not opstack.isempty() and isAlpha(token.lower()) and bidmas[tmp] > bidmas[token]:
                    postfix.append(opstack.pop())
                    tmp = opstack.peek()
            opstack.push(token)

    while not opstack.isempty():
        postfix.append(opstack.pop())

    return postfix

def calculatePostfix(tokens):
    """Take the tokens passed in and calculate them in postfix notation"""
    stack = []
    for token in tokens:
        if isAlpha(token):
            stack.append(token)
            continue

        right = toNum(stack.pop())
        left = toNum(stack.pop())

        if token == '+':
            stack.append(left + right)
        elif token == '-':
            stack.append(left - right)
        elif token == '*':
            stack.append(left * right)
        elif token == '/':
            stack.append(left / right)

    return stack.pop()

def toNum(string):
    """Convert string to an appropriate numerical data type"""
    try:
        return int(string)
    except ValueError:
        return float(string)


def calculate(string):
    """Pipe string through conversion functions and receive output of mathematical operations"""
    return calculatePostfix(toPostfix(tokenise(string)))


if __name__ == "__main__":
    while True:
        infix = input("Enter an equation: ")
        print(calculate(toPostfix(tokenise(infix))))
