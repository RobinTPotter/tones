# values of resistors

x = [1, 2, 4, 8, 16, 32, 64, 128, 256]

# reciprocal values
y = [1/xx for xx in x]

# sum of which gets resistance of parallel when "on"


def dec(xx):
 # return components of x ("binary")
 comp = []
 for cc in range(len(x)-1,-1,-1):
  c = x[cc]
  if xx>=c:
   comp.append(c)
   xx -= c
 return comp

def decR(xx):
 # return components of y
 comp = []
 for cc in range(len(y)):
  if xx==0: break
  c = y[cc]
  if 1/xx<=1/c:
   comp.append(c)
   xx -= c
 return comp
