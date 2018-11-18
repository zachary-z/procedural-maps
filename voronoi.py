import vector
import graph
import math

def Delaunay(points):
	# Step 0: initialize list and add initial triangle
    triangulation = {}
    super_triangle = Tri(Vertex(-1000,0),Vertex(1000,0),Vertex(500,1500))
    triangulation[super_triangle] = False
    # Step 1: add each point and recaculate delaunay triangulation
    for vertex in points:
        # Step 1.1: determine which triangles need replacing
        for triangle in triangulation:
            triangle.circumcircle()
            if vertex.dist(triangle.ccenter) < triangle.cradius:
                triangulation[triangle] = True
        # Step 1.2: determine edge of polygonal hole
        polygon = []
        for triangle in triangulation:
            if triangulation[triangle] == True:
                for edge in triangle.e:
                    shared = False
                    for triangle2 in remove_from_dict(triangulation, triangle):
                        for edge2 in triangle2.e:
                            if edge == edge2 and triangulation[triangle2] == True:
                                shared = True
                    if not shared:
                        polygon.append(edge)
        # Step 1.3: remove the triangles that need replacing
        temporary_triangulation = {}
        for triangle in triangulation:
            if triangulation[triangle] == False:
                temporary_triangulation[triangle] = False
        triangulation = temporary_triangulation
        # Step 1.4: add in the fixed triangles
        for edge in polygon:
            triangle = Tri(vertex, edge.a, edge.b)
            triangulation[triangle] = False
    # Step 2: remove triangles that include vertices in the super-triangle
    temporary_triangulation = {}
    for triangle in triangulation:
        good = True
        for vertex in triangle.v:
            for super_vertex in super_triangle.v:
                if vertex == super_vertex:
                    good = False
        if good == True:
            temporary_triangulation[triangle] = False
    triangulation = temporary_triangulation
    return [triangle for triangle in triangulation]
	
class Voronoi_Tiling:
	def __init__(self, vertices):
		self.vertices = vertices
		self.delaunay = Delaunay(self.vertices)
