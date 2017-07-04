import csv
import json

with open('ao1960200term5skim15000bandwidthNodes.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
f.close()

with open('ao1960200term5skim15000bandwidthNodes.json', 'w+') as f:
    json.dump(rows, f)
f.close()

