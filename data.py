import urllib2
import json


idps = {}

N=2000
while N != 2014:
	response = urllib2.urlopen('http://data.unhcr.org/api/stats/persons_of_concern.json?year='+str(N)+'&country_of_origin=COL&country_of_residence=COL')
	data = json.load(response)
	data = data[0]
	idps[N] = int(data["total_population"])
	N+=1
	
jsondata=json.dumps([{'year': k, 'population': v} for k,v in idps.items()], indent=4, separators=(',', ': '))
print jsondata

f = open('data.json', 'w')
print >> f, jsondata
f.close()




