import requests
import urllib.request
import os
import json

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)

new_sets = []

s = requests.get("https://thepeeps191.github.io/api/sets.json").json()
for i in s:
	y = i
	y["id"] = y["id"].replace("pt", "")
	l = y["legalities"]
	y["legalities"] = []
	for ll in l:
		y["legalities"].append(ll)
	del y["updatedAt"]
	os.mkdir(y["id"])
	urllib.request.urlretrieve(y["images"]["symbol"], y["images"]["symbol"].replace("https://images.pokemontcg.io/", "").replace("pt", ""))
	urllib.request.urlretrieve(y["images"]["logo"], y["images"]["logo"].replace("https://images.pokemontcg.io/", "").replace("pt", ""))
	y["images"]["symbol"] = y["images"]["symbol"].replace("images.pokemontcg.io/", "thepeeps191.github.io/api/").replace("pt", "")
	y["images"]["logo"] = y["images"]["logo"].replace("images.pokemontcg.io/", "thepeeps191.github.io/api/").replace("pt", "")
	new_sets.append(y)
	print("Done:", y["id"])

with open("new_sets.json", "w") as f:
	try:
		json.dump(new_sets, f, indent = 4)
	except Exception:
		json.dump(new_sets, f)