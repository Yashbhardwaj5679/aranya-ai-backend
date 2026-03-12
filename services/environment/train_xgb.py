import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("services/environment/plant_environment_dataset.csv")

print("Dataset shape:", df.shape)
print(df.head())

# -------------------------
# Encode categorical features
# -------------------------

label_encoders = {}

categorical_columns = ["plant", "soil", "season"]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# -------------------------
# Features / target
# -------------------------

X = df.drop("suitable", axis=1)
y = df["suitable"]

# -------------------------
# Train test split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# -------------------------
# XGBoost model
# -------------------------

model = xgb.XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(X_train, y_train)

# -------------------------
# Evaluate
# -------------------------

preds = model.predict(X_test)

accuracy = accuracy_score(y_test, preds)

print("\nEnvironment Model Accuracy:", accuracy)

# -------------------------
# Save model
# -------------------------

joblib.dump(model, "services/environment/environment_model.pkl")

# Save encoders
joblib.dump(label_encoders, "services/environment/encoders.pkl")

print("\nModel saved:")
print("services/environment/environment_model.pkl")