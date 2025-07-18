import streamlit as st
import pandas as pd
import joblib
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Salary Predictor", layout="wide")

# Custom styling for sidebar
st.markdown("""
    <style>
    .css-1d391kg {
        background-color: white !important;
    }
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg p, .css-1d391kg div, .css-1d391kg span {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load the trained model and feature list
model = joblib.load("salary_model.pkl")
with open("model_features.json", "r") as f:
    feature_order = json.load(f)

# Label mappings used during training
experience_levels = {
    "Entry-level (0–1 years)": 0,
    "Mid-level (2–4 years)": 1,
    "Senior-level (5–8 years)": 2,
    "Executive (9+ years)": 3
}

employment_types = {
    "Full-time (FT)": 0,
    "Part-time (PT)": 1,
    "Contract (CT)": 2,
    "Freelance (FL)": 3
}

company_sizes = {
    "Small (1–50) - e.g., Local Startups": 0,
    "Medium (51–250) - e.g., Dunzo, Postman": 1,
    "Large (251+) - e.g., Google, Infosys": 2
}

locations = {
    "India": 0,
    "United States": 1,
    "Germany": 2,
    "Canada": 3,
    "France": 4,
    "Other": 5
}

job_titles = {
    "Data Scientist": 0,
    "Machine Learning Engineer": 1,
    "Data Analyst": 2,
    "Research Scientist": 3,
    "AI Engineer": 4,
    "Data Engineer": 5,
    "Business Analyst": 6,
    "Other": 7
}

currency_rates = {
    "USD (US Dollar)": (1.00, "$"),
    "INR (Indian Rupee)": (83.00, "₹"),
    "GBP (British Pound)": (0.77, "£"),
    "EUR (Euro)": (0.92, "€"),
    "CAD (Canadian Dollar)": (1.36, "CA$"),
    "JPY (Japanese Yen)": (157.00, "¥")
}

# Sidebar content
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg", width=150)
    st.markdown("### 🔍 About")
    st.write("This project predicts tech salaries using global data.")
    st.write("Created for IBM SkillsBuild Internship")

# Title and intro
st.title("💼 Employee Salary Prediction App")
st.caption("📅 Based on 2025 data | 🌍 Global Dataset")

# Tabbed interface
tab1, tab2 = st.tabs(["🔮 Salary Predictor", "📊 Visual Insights"])

with tab1:
    st.subheader("Enter employee details")

    col1, col2 = st.columns(2)
    with col1:
        experience_level = st.selectbox("👤 Experience Level", list(experience_levels.keys()))
        employment_type = st.selectbox("🧾 Employment Type", list(employment_types.keys()))
        job_title = st.selectbox("💼 Job Title", list(job_titles.keys()))
        remote_option = st.radio("🏠 Remote Work Type", ["Fully On-site (0%)", "Hybrid (50%)", "Fully Remote (100%)"])
    with col2:
        company_size = st.selectbox("🏢 Company Size", list(company_sizes.keys()))
        employee_residence = st.selectbox("🌍 Employee Residence", list(locations.keys()))
        company_location = st.selectbox("📍 Company Location", list(locations.keys()))
        currency = st.selectbox("💱 Preferred Currency", list(currency_rates.keys()))

    remote_ratio_mapping = {
        "Fully On-site (0%)": 0,
        "Hybrid (50%)": 50,
        "Fully Remote (100%)": 100
    }
    remote_ratio = remote_ratio_mapping[remote_option]

    # Prepare the input data for prediction
    input_dict = {
        'work_year': 2025,
        'experience_level': experience_levels[experience_level],
        'employment_type': employment_types[employment_type],
        'job_title': job_titles[job_title],
        'remote_ratio': remote_ratio,
        'company_size': company_sizes[company_size],
        'employee_residence': locations[employee_residence],
        'company_location': locations[company_location]
    }

    input_data = pd.DataFrame([input_dict])[feature_order]

    # Perform salary prediction
    if st.button("💸 Predict Salary"):
        prediction_usd = model.predict(input_data)[0]
        rate, symbol = currency_rates[currency]
        converted_annual = prediction_usd * rate
        converted_monthly = converted_annual / 12

        st.success("✅ Predicted Salary")
        st.markdown(f"- Annual: **{symbol}{converted_annual:,.2f}**")
        st.markdown(f"- Monthly: **{symbol}{converted_monthly:,.2f}**")
        st.info("📌 Note: This prediction is based on international salary data. INR and other currencies are converted for your reference.")

with tab2:
    st.subheader("📊 Visual Analysis from Dataset")
    df = pd.read_csv("cleaned_salary_dataset.csv")
    job_title_mapping = {v: k for k, v in job_titles.items()}
    df["job_title_label"] = df["job_title"].map(job_title_mapping)
    exp_mapping = {v: k for k, v in experience_levels.items()}
    df["experience_label"] = df["experience_level"].map(exp_mapping)

    # Average salary by job title
    st.markdown("#### 💼 Average Salary by Job Title")
    avg_salary_by_title = df.groupby("job_title_label")["salary_in_usd"].mean().sort_values()
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    sns.barplot(x=avg_salary_by_title.values, y=avg_salary_by_title.index, ax=ax1, palette="Blues_r")
    ax1.set_xlabel("Average Salary (USD)")
    ax1.set_ylabel("Job Title")
    st.pyplot(fig1)

    # Salary distribution by experience level
    st.markdown("#### 📈 Salary by Experience Level")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="experience_label", y="salary_in_usd", data=df, palette="Set2", ax=ax2)
    ax2.set_xlabel("Experience Level")
    ax2.set_ylabel("Salary (USD)")
    st.pyplot(fig2)

    # Salary trend by experience level
    st.markdown("#### 📉 Salary Trend by Experience")
    salary_by_exp = df.groupby("experience_level")["salary_in_usd"].mean().reset_index()
    salary_by_exp["experience_label"] = salary_by_exp["experience_level"].map(exp_mapping)
    fig3, ax3 = plt.subplots()
    sns.lineplot(data=salary_by_exp, x="experience_label", y="salary_in_usd", marker="o", ax=ax3)
    ax3.set_ylabel("Average Salary (USD)")
    ax3.set_xlabel("Experience Level")
    st.pyplot(fig3)
