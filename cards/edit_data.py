import os
import json

os.mkdir("new_cards")

for file in os.listdir():
	with open(file, encoding = "utf8") as f:
		x = json.load(f)
	for i in x:
		i["id"] = i["id"].replace("pt", "")
		i["legalities"] = [j for j in i["legalities"]]
	with open(f"new_cards/{file.replace('pt', '')}", "w", encoding = "utf8") as f:
		json.dump(x, f, indent = 4)
	print("Done:", file)