fname = "poi_names.txt"

fh = open(fname)
poiCount = 0
lineCount = 0


for line in fh :
	line = line.rstrip()
	lineCount = lineCount + 1
	if line.startswith('(y)') :
		poiCount = poiCount + 1

print poiCount
print lineCount