# -*- coding: cp1252 -*-

import igraph as ig
import random
from json import loads

# with open("MetalGearJp.json") as of:
	# data = loads( of.readline() )

# vertices = random.randint(0,10000)
# lineas   = []

# g = ig.Graph()

# for vert in range(vertices-1):
	# tmp = (vert, vert+1)
	# lineas.append(tmp)

# g.add_vertices(vertices)
# g.add_edges(lineas)
# ig.plot(g)

json1 = "MetalGearJp.json"
json2 = "KonamiJp.json"
with open(json1) as of:
    data1=loads(of.readline())
with open(json2) as of:
    data2=loads(of.readline())
 
data1_mes = []
data2_mes = []
for i in range(len(data1)):
	fecha = data1[i][u'created_time'].strip().split('-')
	if (u'2015' == fecha[0]):
		if int(fecha[1]) in range(9,13):
			data1_mes.append(data1[i])
			
	elif (u'2016' == fecha[0]):
		if int(fecha[1]) in range(1,9):
			data1_mes.append(data1[i])

for i in range(len(data2)):
	fecha = data2[i][u'created_time'].strip().split('-')
	if (u'2015' == fecha[0]):
		if int(fecha[1]) in range(8,13):
			data2_mes.append(data1[i])
			
	elif (u'2016' == fecha[0]):
		if int(fecha[1]) in range(1,8):
			data2_mes.append(data1[i])
 
posts_al_mes1 = int(round(len(data1_mes)/12.0))
posts_al_mes2 = int(round(len(data2_mes)/12.0))
 
print "Numero de posts al mes:\n    ", json1, ":", posts_al_mes1, "\n    ", json2, ":", posts_al_mes2