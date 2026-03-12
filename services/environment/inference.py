import joblib
import pandas as pd

# -----------------------------
# Load model and encoders
# -----------------------------

model = joblib.load("services/environment/environment_model.pkl")
encoders = joblib.load("services/environment/encoders.pkl")


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

    # Encode categorical features

    plant_encoded = encoders["plant"].transform([plant])[0]
    soil_encoded = encoders["soil"].transform([soil])[0]
    season_encoded = encoders["season"].transform([season])[0]

    # Create dataframe

    input_data = pd.DataFrame([{
        "plant": plant_encoded,
        "soil": soil_encoded,
        "temperature": temperature,
        "humidity": humidity,
        "rainfall": rainfall,
        "season": season_encoded
    }])

    # Predict probability

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