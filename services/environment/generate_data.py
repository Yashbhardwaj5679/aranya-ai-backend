import random
import pandas as pd

plants = [
    "tulsi",
    "neem",
    "amla",
    "aloe_vera",
    "ashwagandha",
    "lemongrass",
    "brahmi",
    "giloy",
    "turmeric",
    "bael"
]

soil_types = ["sandy", "loamy", "clay"]
seasons = ["summer", "monsoon", "winter"]

data = []

for _ in range(10000):

    plant = random.choice(plants)
    soil = random.choice(soil_types)
    season = random.choice(seasons)

    temp = random.uniform(10, 45)
    humidity = random.uniform(20, 90)
    rainfall = random.uniform(10, 250)

    # Simple suitability logic
    suitable = 0

    if plant == "neem" and soil in ["sandy", "loamy"] and temp > 20:
        suitable = 1

    if plant == "tulsi" and soil == "loamy" and humidity > 40:
        suitable = 1

    if plant == "lemongrass" and rainfall > 60:
        suitable = 1

    if plant == "turmeric" and season == "monsoon":
        suitable = 1

    if plant == "ashwagandha" and soil == "sandy":
        suitable = 1

    if plant == "aloe_vera" and rainfall < 100:
        suitable = 1

    if plant == "amla" and soil == "loamy":
        suitable = 1

    if plant == "brahmi" and humidity > 60:
        suitable = 1

    if plant == "giloy" and season == "monsoon":
        suitable = 1

    if plant == "bael" and temp > 25:
        suitable = 1

    data.append([
        plant,
        soil,
        temp,
        humidity,
        rainfall,
        season,
        suitable
    ])

df = pd.DataFrame(data, columns=[
    "plant",
    "soil",
    "temperature",
    "humidity",
    "rainfall",
    "season",
    "suitable"
])

df.to_csv("services/environment/plant_environment_dataset.csv", index=False)

print("Dataset generated with", len(df), "rows")