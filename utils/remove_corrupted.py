import os
from PIL import Image

folder = "data/raw/amla"   # change per plant

removed = 0

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    try:
        img = Image.open(path)
        img.verify()
    except:
        os.remove(path)
        removed += 1

print("Removed corrupted images:", removed)