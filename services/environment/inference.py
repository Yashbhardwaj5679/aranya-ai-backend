import joblib
import pandas as pd
import os

# -----------------------------
# Resolve model path safely
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "environment_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "encoders.pkl")

# -----------------------------
# Load model and encoders
# -----------------------------

model = joblib.load(MODEL_PATH)
encoders = joblib.load(ENCODER_PATH)


# -----------------------------
# Prediction function
# -----------------------------

def predict_environment(
    plant,
    soil,
    temperature,
    humidity,
    rainfall,
    season
):

    plant_encoded = encoders["plant"].transform([plant])[0]
    soil_encoded = encoders["soil"].transform([soil])[0]
    season_encoded = encoders["season"].transform([season])[0]

    input_data = pd.DataFrame([{
        "plant": plant_encoded,
        "soil": soil_encoded,
        "temperature": temperature,
        "humidity": humidity,
        "rainfall": rainfall,
        "season": season_encoded
    }])

    probability = model.predict_proba(input_data)[0][1]

    return float(probability)


# -----------------------------
# Manual test
# -----------------------------

if __name__ == "__main__":

    score = predict_environment(
        plant="neem",
        soil="loamy",
        temperature=34,
        humidity=60,
        rainfall=80,
        season="summer"
    )

    print("Suitability Score:", score)