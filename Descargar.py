# -*- coding: cp1252 -*-
#time.mktime(datetime.datetime.strptime("2012-10-25T13:54:34","%Y-%m-%dT%H:%M:%S").timetuple())
#python3
import os
import urllib2
import json
import unicodedata
import requests
#ACCESS TOKEN
at=""
#ID DE PAGINA
face=1574014342849506 #124224143270 HdC
#NOMBRE DE PAGINA
fname="abcd" #hdecristo HdC


link="https://graph.facebook.com/"+str(face)+"?access_token="+at+"&"
opts="fields=description,name,about,feed.limit(50){likes.limit(50).summary(True){id,name},comments.limit(50).summary(True){from,message},from,type,message,shares,created_time},likes"
link=link+opts

#print "Abriendo",link
with requests.Session() as session:
	session.get("https://graph.facebook.com/?access_token="+at)
	algo = session.get(link).text
	#algo=urllib2.urlopen(link)
	#print "Link listo"
	megalin=""
	posts=[]
	#print link
	for x in range(0,1000):
	#    algo=urllib2.urlopen(link,timeout=3600)
			algo = session.get(link).text
			
			for linea in algo:
				linea=linea.replace("\n","").replace("    ","");
				megalin+=linea;
			datos=json.loads(megalin)
		#print datos.keys()
			if "paging" not in datos and x!=0:
			#print "Saliendo"
				break
			if x==0:
				posts+=datos["feed"]["data"]
				link=datos["feed"]["paging"]["next"]
			#print link
			else:
				posts+=datos["data"]
				link=datos["paging"]["next"]
			#print link
			megalin=""
			linea=""
		#print (x+1)*100

	print "Recopilando nombres de likes"
	tempurl=""
	for pind in xrange(len(posts)):
		if "likes" in posts[pind]:
			if "paging" in posts[pind]["likes"]:
				if "next" in posts[pind]["likes"]["paging"]:
					tempdata=""
					tempurl=posts[pind]["likes"]["paging"]["next"]
					#print "+ Likers"
					while tempdata=="":
						#new=urllib2.urlopen(tempurl)
						new=session.get(tempurl).text
						for linea in new:
							linea=linea.replace("\n","").replace("    ","")
							tempdata+=linea
						pers=json.loads(tempdata)
						posts[pind]["likes"]["data"]+=pers["data"]
						if "next" in pers["paging"]:
							tempurl=pers["paging"]["next"]
							#print "++ likers"
							tempdata=""
							#print pind

	print "Reuniendo comentarios"
	
	for pind in xrange(len(posts)):
		if "comments" in posts[pind]:
			if "paging" in posts[pind]["comments"]:
				if "next" in posts[pind]["comments"]["paging"]:
					tempdata=""
					tempurl=posts[pind]["comments"]["paging"]["next"]
					#print tempurl,"+ coments"
					while tempdata=="":
						#new=urllib2.urlopen(tempurl)
						new=session.get(tempurl).text
						for linea in new:
							linea=linea.replace("\n","").replace("    ","")
							tempdata+=linea
						pers=json.loads(tempdata)
						posts[pind]["comments"]["data"]+=pers["data"]
						if "next" in pers["paging"]:
							tempurl=pers["paging"]["next"]
							#print tempurl,"++ coments"
							tempdata=""

archi=open(fname+".json","w")
archi.write(json.dumps(posts))
print "Escrito",fname
archi.close()