import json
from PIL import Image
class Process():
    res = (1920, 1080)
    with open("imgs.json") as json_data:
        data = json.load(json_data)
    images = list(data.keys())
    for img in images:
        if int(data[img]["length"]) > 1000 and int(data[img]["width"]) > 540:
            currentImage = Image.open("img/" + img + ".jpg")
            resizedImage = currentImage.resize(res)
    #TODO: replace resize algorithm with seam carving algorithm
p = Process()
