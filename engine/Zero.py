

#  This defines a polymorphic Zero value

class Zero:
    def __str__(self):
	  return "0"
    def __add__(self, y):
	  return y
    def __radd__(self, y):
	  return y
    def __sub__(self, y):
      return -y
    def __rsub__(self, y):
      return y
    def __mul__(self, y):
      return self
    def __rmul__(self, y):
      return self
    def __abs__(self):
      return self
    def __neg__(self):
      return self

    # Todo - worry about Zero in other contexts

zero = Zero()
zero.x = 0
zero.y = 0
zero.z = 0
zero.h = 0
zero.p = 0
zero.r = 0



