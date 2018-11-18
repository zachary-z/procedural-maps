import math
import vector

class Vertex:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.vec = vector.vector(x,y,0)
	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False
	def dist(self, other):
		return self.vec.dist(other.vec)

class Edge:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __len__(self):
		return self.a.vec.dist(self.b.vec)
	def __eq__(self, other):
		if (self.a == other.a and self.b == other.b) or (self.a == other.b and self.b == other.a):
			return True
		else:
			return False

class Graph:
	def __init__(self, vertices, edges):
		self.v = vertices
		self.e = edges
	def __eq__(self, other):
		if self.e == other.e and self.v == other.v:
			return True
		else:
			return False
	def connected_vertices(self):
		connected = {}
		for v in self.v:
			connected[v] = []
			for e in self.e:
				if e.a == v:
					connected[v].append(e.b)
				elif e.b == v:
					connected[v].append(e.a)
		return connected
		
class Polygon(Graph):
	def __init__(self, vertices):
		edges = [Edge(vertices[i], vertices[(i+1)%len(vertices)]) for i in range(len(vertices))]
		Graph.__init__(self, vertices, edges)
		self.centroid = Vertex(sum([v.x for v in self.v])/len(self.v), sum([v.y for v in self.v])/len(self.v))
		
class Triangle(Polygon):
	def __init__(self, a, b, c):
		Polygon.__init__(self, [a,b,c])
		self.circumcenter = Vertex(0,0)
		self.circumradius = 0
	def circumcircle(self):
		a = self.v[0]
        b = self.v[1]
        c = self.v[2]
        # sidelengths
        A = c.dist(b)
        B = a.dist(c)
        C = b.dist(a)
        # useful constant
        d = 2*(a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y))
        # coordinates
        x = 0
        x += (a.x**2+a.y**2)*(b.y-c.y)
        x += (b.x**2+b.y**2)*(c.y-a.y)
        x += (c.x**2+c.y**2)*(a.y-b.y)        
        y = 0
        y += (a.x**2+a.y**2)*(b.x-c.x)
        y += (b.x**2+b.y**2)*(c.x-a.x)
        y += (c.x**2+c.y**2)*(a.x-b.x)

        try: self.cradius = A*B*C/math.sqrt((A+B+C)*(A+B-C)*(A-B+C)*(-A+B+C))
        except ZeroDivisionError: self.cradius = 10000000
        try: self.ccenter = Vertex(x/d, -y/d)
        except ZeroDivisionError: self.ccenter = Vertex(1000000,1000000)
