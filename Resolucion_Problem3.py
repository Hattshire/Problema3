#Julian Sepulveda
#Sebastian Landero
#Gustavo Valladares

import igraph as ig
from json import loads
json1 = "MetalGearJp.json"
json2 = "KonamiJp.json"
with open(json1) as of:
    data1=loads(of.readline())
with open(json2) as of:
    data2=loads(of.readline())

data1_anno = []
data2_anno = []

for i in range(len(data1)):
    fecha = data1[i][u'created_time'].strip().split('-')
    if (u'2015' == fecha[0]):
        if int(fecha[1]) in range(8,13):
            data1_anno.append(data1[i])
           
    elif (u'2016' == fecha[0]):
        if int(fecha[1]) in range(1,8):
            data1_anno.append(data1[i])
 
for i in range(len(data2)):
    fecha = data2[i][u'created_time'].strip().split('-')
    if (u'2015' == fecha[0]):
        if int(fecha[1]) in range(8,13):
            data2_anno.append(data2[i])
           
    elif (u'2016' == fecha[0]):
        if int(fecha[1]) in range(1,8):
            data2_anno.append(data2[i])

posts_al_mes1 = int(round(len(data1_anno)/12.0))
posts_al_mes2 = int(round(len(data2_anno)/12.0))

print "Numero de posts al mes:\n ", json1, ":", posts_al_mes1, "[posts/mes]\n ", json2, ":", posts_al_mes2, "[posts/mes]"

suma_likes1 = 0
suma_comments1 = 0
suma_likes2 = 0
suma_comments2 = 0

for j in range(len(data1_anno)):
    suma_likes1 += int(data1_anno[j]['likes']['summary']['total_count'])
    suma_comments1 += int(data1_anno[j]['comments']['summary']['total_count'])

for b in range(len(data2_anno)):
    suma_likes2 += int(data2_anno[b]['likes']['summary']['total_count'])
    suma_comments2 += int(data2_anno[b]['comments']['summary']['total_count'])

likes_al_mes1 = int(round(suma_likes1/12.0))
comments_al_mes1 = int(round(suma_comments1/12.0))
likes_al_mes2 = int(round(suma_likes2/12.0))
comments_al_mes2 = int(round(suma_comments2/12.0))

print "\nLikes y Comments al mes:\n", json1, ":\n ", likes_al_mes1, "[likes/mes]\n ", comments_al_mes1, "[comments/mes]\n", json2, ":\n ", likes_al_mes2, "[likes/mes]\n ", comments_al_mes2, "[comments/mes]"

persons_like1 = set()
persons_comment1 = set()
persons_like2 = set()
persons_comment2 = set()


for k in range(len(data1_anno)):
    for w in range(len(data1_anno[k]['likes']['data'])):
        persons_like1.add(data1_anno[k]['likes']['data'][w]['id'])
    for x in range(len(data1_anno[k]['comments']['data'])):
        persons_comment1.add(data1_anno[k]['comments']['data'][x]['from']['id'])

for l in range(len(data2_anno)):
    for y in range(len(data2_anno[l]['likes']['data'])):
        persons_like2.add(data2_anno[l]['likes']['data'][y]['id'])
    for z in range(len(data2_anno[l]['comments']['data'])):
        persons_comment2.add(data2_anno[l]['comments']['data'][z]['from']['id'])

persons1 = len(persons_like1&persons_comment1)
persons2 = len(persons_like2&persons_comment2)

persons_al_mes1 = int(round(persons1/12.0))
persons_al_mes2 = int(round(persons2/12.0))

print "\nPersonas que dan like y comments al mes:\n ", json1, ":", persons_al_mes1, "[personas/mes]\n ", json2, ":", persons_al_mes2, "[personas/mes]"

data1_mes = []
data2_mes = []

for i in range(len(data1)):
    if "2016-08-" in data1[i]['created_time']:
        data1_mes.append(data1[i])
for i in range(len(data2)):
    if "2016-08-" in data2[i]['created_time']:
        data2_mes.append(data2[i])

persons_like_mes1 = set()
persons_like_mes2 = set()

for k in range(len(data1_mes)):
    for w in range(len(data1_mes[k]['likes']['data'])):
        persons_like_mes1.add(data1_mes[k]['likes']['data'][w]['name'])
for l in range(len(data2_mes)):
    for y in range(len(data2_mes[l]['likes']['data'])):
        persons_like_mes2.add(data2_mes[l]['likes']['data'][y]['name'])

g = ig.Graph()

g.add_vertex("MetalGearJp", color="black", size=100)
g.add_vertex("KonamiJp", color="pink", size=150)

#Se itera sobre las ids de las personas que han puesto like
#Esta id se mantiene en vert
#Luego se anyade el vertice usando un color cercano al turquesa 
for vert in (persons_like_mes1 | persons_like_mes2):
    g.add_vertex(vert, color="#00bbff")

#Se itera sobre las ids de las personas que les gusta la pagina 1
#Se almacena en vert i se añade una linea o arista entre la bola
#de la pagina 1 y vert
for vert in (persons_like_mes1):
    g.add_edge(vert,"MetalGearJp")

#Se itera sobre las ids de las personas que les gusta la pagina 2
#Se almacena en vert i se añade una linea o arista entre la bola
#de la pagina 2 y vert
for vert in (persons_like_mes2):
    g.add_edge(vert,"KonamiJp")
#Se genera una imagen del grafico a un tamaño personalizado y de fondo color plomo     
ig.plot(g, bbox=(1920,1080), background="#171717")

