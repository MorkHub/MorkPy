_store = {}
 _store['input'] = input
 
 print('MorkPy imported. https://github.com/MorkHub/MorkPy')
 def input (prompt='Input a number: ',type=int,error='Error - Wrong Type'):
      temp = None
      while temp is None:
          try:
              temp = type(_store['input'](str(prompt)))
          except ValueError:
              print(error)
              continue
      return temp
