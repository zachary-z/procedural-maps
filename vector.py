import math

class vector:
    def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, v):
        return vector(self.x+v.x, self.y+v.y, self.z+v.z)
    def __radd__(self, v):
        return vector(v.x+self.x, v.y+self.y, v.z+self.z)
    def __sub__(self, v):
        return vector(self.x-v.x, self.y-v.y, self.z-v.z)
    def __rsub__(self, v):
        return vector(v.x-self.x, v.y-self.y, v.z-self.z)
    # Scalar multiplication and division, vector dot product
    def __mul__(self, sorv):
        if isinstance(sorv, (float, int)):
            return vector(self.x*sorv, self.y*sorv, self.z*sorv)
        else:
            return self.x*sorv.x + self.y*sorv.y + self.z*sorv.z
    def __rmul__(self, sorv):
        if isinstance(sorv, (float, int)):
            return vector(self.x*sorv, self.y*sorv, self.z*sorv)
        else:
            return self.x*sorv.x + self.y*sorv.y + self.z*sorv.z
    def __truediv__(self, s):
        if isinstance(s, (float, int)):
            return vector(self.x/s, self.y/s, self.z/s)
        else:
            return self
    # Vector cross products
    def __xor__(self, v):
        return vector(self.y*v.z - self.z*v.y,
                      self.z*v.x - self.x*v.z,
                      self.x*v.y - self.y*v.x)
    def normalize(self):
        mag = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return self/mag
    # Miscellaneous
    def __neg__(self):
        return -1*self
    def __pos__(self):
        return self
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    '''
    ATTRIBUTES
    - angle
    - distance
    - indexing
    '''
    def angle(self):
        return math.atan2(self.y, self.x)
    def dist(self, v):
        return abs(self-v)
    def __getitem__(self, index):
        return [self.x, self.y, self.z][index]
    def __str__(self):
        return 'Vector: ('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
