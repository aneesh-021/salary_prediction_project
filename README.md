 💼 Salary Predictor using Machine Learning

A simple yet effective web app built with Streamlit that predicts employee salaries based on various features such as experience level, employment type, company size, and more. It also includes salary visualization and international currency support.



 🧠 Features

 📊 Predicts salaries using a trained regression model
 🌍 Supports multiple currencies (USD, INR, EUR, GBP, CAD)
 𞴩‍💼 Categorizes experience: Fresher, Mid-level, Senior, Executive
 🏢 Takes into account company size (with real-world examples)
 📈 Visualizes experience vs salary with a line chart
 📒 Notes that dataset is based on international market data



 📂 Project Structure

```
Salary-Predictor-AI/
│
├── app.py               # Main Streamlit app
├── model.pkl            # Trained machine learning model
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── data.csv             # (Optional) Original dataset
```



 📅 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/Salary-Predictor-AI.git
cd Salary-Predictor-AI
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app

```bash
streamlit run app.py
```



 🌐 Supported Currencies

 🇺🇸 USD (Default dataset currency)
 🇮🇳 INR
 🇪🇺 Euro (EUR)
 🇬🇧 Pound Sterling (GBP)
 🇨🇦 Canadian Dollar (CAD)

> 💡 Note: All predictions are based on an international dataset (mostly U.S. based). Currency conversion is approximate and for reference only.



 🧪 Model Information

 Algorithm: Linear Regression
 Training Dataset: \[data.csv] (based on international data)
 Input Features:

   Experience Level
   Employment Type
   Company Size
   Job Title
   Remote Work Ratio
   Country



📈 Sample Visualization

A line chart showing Years of Experience vs Predicted Salary is included to help users understand salary growth trends visually.

---

 🧑‍💻 Future Scope

This is a base version of the project. Upcoming features (in progress or planned):

 🧯 Add user login and dashboard (for salary history)
 🏢 Company-wise salary comparison
 🌤️ Support for multiple languages
 🎯 Improved UI/UX design



🎓 Built For

This project was developed as part of the IBM SkillsBuild Internship Program, focused on applying data science and machine learning concepts in real-world use cases.



👨‍💼 Author

Aneesh Desai
B.Tech Student | Data Science Enthusiast | Learning Python, ML & UI/UX
