import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("ds_salaries.csv")  # Make sure filename matches

# Drop columns you won't use
df.drop(columns=["salary", "salary_currency"], inplace=True)

# Check for missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Encode categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Save cleaned dataset
df.to_csv("cleaned_salary_dataset.csv", index=False)
print("✅ Cleaned data saved as cleaned_salary_dataset.csv")
