
import urllib2
import json


Everything = {}
response = urllib2.urlopen('http://data.unhcr.org/api/stats/country_of_residence.json')
data = json.load(response)
for country in data:
	code = country['country_of_residence']
	response = urllib2.urlopen('http://data.unhcr.org/api/stats/persons_of_concern.json?year=2013&country_of_origin='+ code)
	data = json.load(response)
	info = {}
	info["year"] = 2013
	info["total_population"] =0
	info["refugees"] =0
	info["returned_refugees"] = 0
	info["idps"] = 0
	info["asylum_seekers"] = 0

	for i in range (len(data)):
		if data[i]["total_population"] is not None and data[i]["total_population"]!='*':
			info["total_population"] += int(data[i]["total_population"])
		if data[i]["refugees"] is not None:
			info["refugees"] += int(data[i]["refugees"])
		if data[i]["returned_refugees"]  is not None:
			info["returned_refugees"] += int(data[i]["returned_refugees"])
		if data[i]["idps"] is not None:
			info["idps"] += int(data[i]["idps"])
		if data[i]["asylum_seekers"] is not None:
			info["asylum_seekers"] += int(data[i]["asylum_seekers"])
	Everything[code]= info
	print code

jsondata=json.dumps(Everything.values(), indent=4, separators=(',', ': '))


f = open('countries_data.json', 'w')
print >> f, jsondata
f.close()




