class Stack:
  def __init__(self):
    self.items = []

  def push(self,item):
    return self.items.append(item)

  def pop(self):
    try:
      return self.items.pop()
    except:
      return "Empty Stack"
  def is_empty(self):
    return self.items == []

  def peek(self):
    try:
      return self.items[-1]
    except:
      return "Empty Stack"

  def size(self):
    return len(self.items)
