import zipfile
import os
import shutil

path = "" # the path to the jar, to be patched

def extractJar(jar_path, extract_to='.'):
    with zipfile.ZipFile(jar_path, 'r') as jar:
        jar.extractall(extract_to)
            

# Example usage
extractJar(path, './tmp')
with open(r"./tmp/data/ad_astra/planets/earth.json") as f:
      data = f.readlines()


lte = 0
for i in data:
    if "\"oxygen\": true" in i:
        print(i)
        break
    lte = lte + 1 

data[lte] = "  \"oxygen\": false, \n"
with open('stats.txt', 'w') as file:
    file.writelines( data )

with open("./tmp/data/ad_astra/planets/earth.json", "w") as f:
    f.writelines(data)

shutil.make_archive("ad_astra-fabric-1.20.1-1.15.20", 'zip', "./tmp")
shutil.move("ad_astra-fabric-1.20.1-1.15.20.zip",path) 
shutil.rmtree("tmp")