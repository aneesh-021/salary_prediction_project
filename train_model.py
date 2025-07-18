import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import json

# Load cleaned dataset
df = pd.read_csv("cleaned_salary_dataset.csv")

# Define features and target
X = df.drop(columns=["salary_in_usd"])
y = df["salary_in_usd"]

# ✅ Print the feature column names (important for Streamlit later)
print("✅ Feature columns used during training:")
print(X.columns.tolist())

# ✅ Save column names to JSON for use in Streamlit app
with open("model_features.json", "w") as f:
    json.dump(X.columns.tolist(), f)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
print("\n📊 Model Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Save the trained model
joblib.dump(model, "salary_model.pkl")
print("\n✅ Model saved as salary_model.pkl")
print("✅ Feature list saved as model_features.json")
