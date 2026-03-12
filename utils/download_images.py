import os
import csv
import requests
from tqdm import tqdm

csv_file = "utils/b.csv"
save_folder = "data/kaggle_upload/neem"

os.makedirs(save_folder, exist_ok=True)

image_urls = []

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get("image_url"):
            image_urls.append(row["image_url"])

image_urls = list(set(image_urls))  # remove duplicates

for i, url in enumerate(tqdm(image_urls)):
    try:
        url = url.replace("square", "large")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(f"{save_folder}/neem_{i+1}.jpg", "wb") as f:
                f.write(response.content)
    except:
        continue

print("Download complete.")