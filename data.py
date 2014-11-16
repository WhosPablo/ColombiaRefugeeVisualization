import urllib2
import json



years = {}

year=2000
while year != 2014:
	response = urllib2.urlopen('http://data.unhcr.org/api/stats/persons_of_concern.json?year='+str(year)+'&country_of_origin=COL')
	data = json.load(response)
	info = {}
	info["year"] = year
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
	years[year]= info
	print info
	print year
	year+=1
print years
jsondata=json.dumps(years.values(), indent=4, separators=(',', ': '))
print jsondata

f = open('data.json', 'w')
print >> f, jsondata
f.close()




