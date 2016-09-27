# -*- coding: cp1252 -*-

import igraph as ig
import random

vertices = random.randint(0,10000)
lineas   = []

g = ig.Graph()

for vert in range(vertices-1):
	tmp = (vert, vert+1)
	lineas.append(tmp)

g.add_vertices(vertices)
g.add_edges(lineas)
ig.plot(g)