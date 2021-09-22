# code to read json and convert into tab delimited txt file

tmp = []
with open('file 01.json', 'r') as jsin:
    for jsonObj in jsin:
        resDict = json.loads(jsonObj)
        tmp.append(resDict)

for d in tmp:        
    fieldnames = d.keys()
    
with open('output01.txt', mode='w', newline='') as csv_file:    
    writer = csv.DictWriter(csv_file, delimiter='\t', fieldnames=fieldnames)
    writer.writeheader()
    for d in tmp:
        writer.writerow(d)
