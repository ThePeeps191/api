import json, urllib.request

setid = "bw7"
apiurl = "https://thepeeps191.github.io/api/"

with open(f"cards/{setid}.json") as f:
	x = json.load(f)

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)

for i in x:
	print(i["name"])
	urllib.request.urlretrieve(i["images"]["small"], i["images"]["small"].replace("pt", "").replace("https://images.pokemontcg.io/", ""))
	urllib.request.urlretrieve(i["images"]["large"], i["images"]["large"].replace("pt", "").replace("https://images.pokemontcg.io/", ""))
	i["images"]["small"] = apiurl + i["images"]["small"].replace("pt", "").replace("https://images.pokemontcg.io/", "")
	i["images"]["large"] = apiurl + i["images"]["large"].replace("pt", "").replace("https://images.pokemontcg.io/", "")

with open(f"cards/{setid}.json", "w") as f:
	json.dump(x, f, indent = 4)