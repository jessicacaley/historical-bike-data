data = {}

for bike in data["bikes"]:
     f= open("%s.json" % bike, "w+")
     f.write(str(data["bikes"][bike]).replace("'", '"'))
     f.close()