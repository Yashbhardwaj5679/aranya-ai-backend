import cv2
import os

folder = "data/raw/aloe_vera"
threshold = 100

removed = 0

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    img = cv2.imread(path)
    if img is None:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    if variance < threshold:
        os.remove(path)
        removed += 1

print("Removed blurry images:", removed)