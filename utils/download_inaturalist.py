import os
import requests
from tqdm import tqdm

# species to download
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


def download_species(common_name, scientific_name, max_images=200):

    print(f"\nDownloading {common_name}")

    folder = os.path.join(SAVE_DIR, common_name)
    os.makedirs(folder, exist_ok=True)

    url = "https://api.inaturalist.org/v1/observations"

    params = {
        "q": scientific_name,
        "quality_grade": "research",
        "photos": "true",
        "per_page": 100
    }

    count = 0
    page = 1

    while count < max_images:

        params["page"] = page

        r = requests.get(url, params=params)
        data = r.json()

        if len(data["results"]) == 0:
            break

        for obs in data["results"]:

            if "photos" not in obs:
                continue

            for photo in obs["photos"]:

                if count >= max_images:
                    break

                img_url = photo["url"].replace("square", "large")

                try:
                    img = requests.get(img_url, timeout=10).content

                    filename = os.path.join(
                        folder,
                        f"{common_name}2_{count}.jpg"
                    )

                    with open(filename, "wb") as f:
                        f.write(img)

                    count += 1

                except:
                    continue

        page += 1

    print(f"Downloaded {count} images")


for plant, sci in plants.items():
    download_species(plant, sci)