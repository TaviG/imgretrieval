
import glob
path = "/home/tavi/Facultate/DATCU/imagini/*/*.jpg"
images = glob.glob(path)

d = {}
clase = []
for img in images:
    clasa = img.split("/")[-2].split("_")[0]
    clase.append(clasa)


for i in range(len(images)):
    if not (clase[i] in d.keys()):
        d[clase[i]] = [images[i]]
    else:
        d[clase[i]].append(images[i])

