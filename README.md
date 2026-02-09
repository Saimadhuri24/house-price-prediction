# 🏠 House Price Prediction Web Application

This project is a **Machine Learning–based House Price Prediction system** with a **Flask web application**, user authentication, and location-based price prediction.  
It predicts house prices in **Bengaluru** based on features like **location, total square feet, BHK, and number of bathrooms**.

---

## 📌 Project Features

- 📊 Machine Learning model trained on real Bengaluru housing data  
- 📍 Location-based price prediction  
- 🔐 User Authentication (Signup / Login / Logout)  
- 🌐 Flask-based web application  
- 🎨 Clean UI using HTML & CSS  
- 💾 Model persistence using Pickle  
- 🧠 Multiple ML algorithms tested and best model selected automatically  

---

## 🛠️ Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Flask  
- SQLite (SQLAlchemy)  
- HTML, CSS  
- Pickle  

---

## 📂 Project Structure

house-price-prediction/
│
├── app.py # Flask backend
├── train_model.py # Model training script
├── bengaluru_house_prices.csv # Dataset
│
├── model/
│ └── best_model.pkl # Saved ML model
│
├── static/
│ └── style.css # CSS styling
│
├── templates/
│ ├── home.html
│ ├── login.html
│ ├── signup.html
│ ├── index.html
│ └── result.html
│
└── README.md


---

## 🧠 Machine Learning Workflow

1. Import required libraries  
2. Load Bengaluru house price dataset  
3. Data cleaning and preprocessing  
4. Feature extraction (location, sqft, BHK, bath)  
5. One-hot encoding for categorical data  
6. Train multiple models:
   - Linear Regression  
   - Decision Tree Regressor  
   - Random Forest Regressor  
   - Gradient Boosting Regressor  
7. Select best model based on **R² score**  
8. Save trained model using Pickle  

---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install pandas numpy scikit-learn flask flask_sqlalchemy werkzeug

2️⃣ Train the Machine Learning Model
python train_model.py
This will:
Train multiple models
Select the best one
Save it as model/best_model.pkl

3️⃣ Run the Flask Application
python app.py

4️⃣ Open in Browser
http://127.0.0.1:5000/

🖥️ Web Application Flow

User signs up / logs in
User enters:
Location
Total square feet
BHK
Bathrooms
ML model predicts house price
Predicted price is displayed on the result page

📊 Evaluation Metric

R² Score (Coefficient of Determination)
The model with the highest R² score is selected as the final model.

🚀 Future Enhancements

📈 Add price trend visualizations
🗺️ Integrate map-based location selection
☁️ Deploy on cloud platforms (Render / Railway / AWS)
📱 Make UI fully responsive
🧠 Add Explainable AI (SHAP) for prediction insights

👩‍💻 Author

Sai Madhuri
House Price Prediction using Machine Learning & Flask
