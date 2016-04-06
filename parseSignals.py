import csv
bssids=[]
individualBssids=[]
locations=[]
individualLocations=[]
newRows=[]

# remove first line
with open("signals.csv",'r') as f:
    with open("updated_signals.csv",'w') as f1:
        f.next() # skip header line
        for line in f:
            f1.write(line)

# collect unique bssids
with open('updated_signals.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		bssids.append(row[0])
		locations.append(row[2])
	for bssid in bssids:
		if bssid not in individualBssids:
			individualBssids.append(bssid);
	for location in locations:
		if location not in individualLocations:
			individualLocations.append(location)
	print(individualBssids)
	print(individualLocations)

# replace bssids with the respective indices
with open('updated_signals.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
		newRows.append([individualBssids.index(row[0]), row[1], individualLocations.index(row[2])])

# create a new file with parsed signals
with open('parsedSignals.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(newRows)
