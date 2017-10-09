import json

fileOpen = open('./netflixData/combined_data_1.json', 'r')
parsed = json.loads(fileOpen)
print (json.dumps(parsed, indent=4, sort_keys=True))
