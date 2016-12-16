class cool:
  def __init__ (self):
    self.value = 'cool'
  def __add__ (self,other):
    return str(self) + ' and ' + str(other)
  def __str__ (self):
    return self.value

class good:
  def __init__ (self):
    self.value = 'good'
  def __add__ (self,other):
    return str(self) + ' and ' + str(other)
  def __str__ (self):
    return self.value

print(cool() + good())
