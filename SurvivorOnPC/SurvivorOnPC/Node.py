class Empty():
  def __init__(self):
    self.IsEmpty = True
  def Map(self, f):
    return AUX_Map(self, f)
  def Filter(self, f):
    return AUX_Filter(self, f)
  def Fold(self, f,z ):
    return AUX_Fold(self, f, z)


class Node():
  def __init__(self, value, tail):
    self.IsEmpty = False
    self.Value = value
    self.Tail = tail
  def Map(self, f):
    return AUX_Map(self, f)
  def Filter(self, f):
    return AUX_Filter(self, f)
  def Fold( self , f, z):
    return AUX_Fold (self, f, z)


def Iterate(l, f):
  if not l.IsEmpty:
    f(l.Value)
    Iterate(l.Tail, f)

def AUX_Map(l, f):
  if not l.IsEmpty:
    return Node(f(l.Value), AUX_Map(l.Tail, f))
  else:
    return Empty

def AUX_Filter(l, f):
  if not l.IsEmpty:
    if f(l.Value) == True:
      return Node(l.Value, AUX_Filter(l.Tail, f))
    else:
      return AUX_Filter(l.Tail, f)
  else:
    return Empty

def AUX_Fold(l,f,z):
  if  l.IsEmpty:
    return z
  else:
    return f(l.Value,AUX_Fold(l.Tail,f,z))
      