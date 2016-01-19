class Empty():
  def __init__(self):
    self.IsEmpty = True

class Node():
  def __init__(self, value, tail):
    self.IsEmpty = Empty
    self.Value = value