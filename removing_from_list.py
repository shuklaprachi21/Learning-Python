n = [1, 3, 5]
print "n:",n
# Remove the first item in the list here
a = n.pop(0)
print "pop(0): returns",a,"n:", n
n = [1, 3, 5]
b = n.remove(1)
print "remove(1): returns",b,"n:", n
n = [1, 3, 5]
del(n[1])
print "del(n[1]):",n