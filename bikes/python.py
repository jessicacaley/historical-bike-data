data = {}


for bike in data["bikes"]:
     f= open("%s.json" % bike, "w+")
     f.write(str(data["bikes"][bike]).replace("'", '"'))
     f.close()


# for i in range(10):
#     f.write("This is line %d\r\n" % (i+1))
