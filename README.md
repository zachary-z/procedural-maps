# procedural-maps

This code creates different Voronoi tilings and Delaunay triangulations using a variety of computational geometry algorithms, including the Bowyer-Watson algorithm.  It uses these to create and draw maps of islands.

The Bowyer-Watson algorithm calculates the Delaunay triangulation of a set of points, which is the triangulation of the convex hull of the points in the diagram in which every circumcircle of a triangle in the diagram is empty.  It does this in n log n time by inserting the points sequentially and recalculating the triangulation.  This is used to find the Voronoi diagram of the points, which is the dual graph of the Delaunay triangulation, and each cell is the set of all points on the plane closest to the center point.  The code takes a while to actually compile and run when there are a sufficient number of points because the edges of the Voronoi diagram must both be calculated and ultimately drawn.  Because of this, pygame is initialized after the larger computations are made.

The points can also be improved by using the centroid of each cell in the Voronoi diagram as the new points for another Voronoi diagram.  This ensures that the points will be less random and more uniformly spaced, leading to more asthetically pleasing diagrams and maps.  This also has the effect of increasing the positions of the points to beyond the bounds of the screen, so a limiting factor had to be implemented as well.

Once the Voronoi diagram is set up, each cell (or land) is designated as either land or water, and the elevation of the lands are then determined by the distance to the shorelines with some random variation.  Lakes and rivers are then added, lakes by random flood filling with a certain probability of stopping and rivers, which start at a vertex above a certain elevation and then go down the steepest slope down to the shoreline.  Humidity at each vertex is then calculated based on the distance to fresh water (lakes and rivers), and then each land cell is designated with a certain biome and color according to their average altitude and humidity, while the lake and ocean cells are colored blue.  Each polygonal cell is then drawn with their colors averaged slightly with their neighbors.

Here are some screenshots of the Voronoi tilings and Delaunay triangulations:

![](https://github.com/zachary-z/procedural-maps/blob/master/centroidvoronoi.png)

![](https://github.com/zachary-z/procedural-maps/blob/master/originalvoronoi.png)

and a tiling with corrected points

![](https://github.com/zachary-z/procedural-maps/blob/master/fixedpointvoronoi.png)
