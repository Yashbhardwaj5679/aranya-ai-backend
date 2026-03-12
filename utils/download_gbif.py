import os
import requests
import pandas as pd
from tqdm import tqdm

plants = {
    "tulsi": "Ocimum tenuiflorum",
    "neem": "Azadirachta indica",
    "aloe_vera": "Aloe vera",
    "giloy": "Tinospora cordifolia",
    "ashwagandha": "Withania somnifera",
    "amla": "Phyllanthus emblica",
    "bael": "Aegle marmelos",
    "brahmi": "Bacopa monnieri",
    "lemongrass": "Cymbopogon citratus",
    "turmeric": "Curcuma longa"
}

SAVE_DIR = "data/raw"
os.makedirs(SAVE_DIR, exist_ok=True)

def download_species(name, scientific):

    folder = os.path.join(SAVE_DIR, name)
    os.makedirs(folder, exist_ok=True)

    url = "https://api.gbif.org/v1/occurrence/search"

    params = {
        "scientificName": scientific,
        "mediaType": "StillImage",
        "limit": 300
    }

    r = requests.get(url, params=params)
    data = r.json()["results"]

    count = 0

    for item in tqdm(data):

        if "media" not in item:
            continue

        for media in item["media"]:

            if "identifier" not in media:
                continue

            try:
                img_url = media["identifier"]
                img = requests.get(img_url, timeout=10).content

                with open(f"{folder}/{name}_{count}.jpg","wb") as f:
                    f.write(img)

                count += 1

            except:
                continue

    print(name, "downloaded:", count)

for plant, sci in plants.items():
    download_species(plant, sci)