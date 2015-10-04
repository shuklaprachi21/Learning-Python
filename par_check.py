from stack import *

def par_check(str):
  s = Stack()
  balanced = None
  for ch in str:
    if ch in "{[(":
      s.push(ch)
    elif ch in ")}]":
      try:
        top = s.pop()
        if matches(top,ch) == False:
          balanced = False
          return balanced
      except:
        balanced = False
        return balanced
    else:
      pass
  if s.is_empty() == False:
    balanced = False
  else:
    balanced = True
  return balanced

def matches(o,c):
  open = "([{"
  close = ")]}"
  return open.index(o) == close.index(c)

