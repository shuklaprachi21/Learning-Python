import sys
from stack import *

def dec_to_bin(dec):
  s = Stack()
  bin_str = ""
  try:
    dec_num = int(dec)
    while dec_num > 0:
      rem = dec_num % 2
      s.push(rem)
      dec_num = dec_num / 2 
    while not s.is_empty():
      bin_str = bin_str + str(s.pop())
    print bin_str
  except:
    print "Enter numbers only"
    sys.exit(0)
  return bin_str
