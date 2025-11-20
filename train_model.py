import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import pickle
import os
import re

# Load dataset
df = pd.read_csv("bengaluru_house_prices.csv")

# Drop rows with missing price
df = df.dropna(subset=['price'])

# Select useful columns
data = df[['location', 'total_sqft', 'size', 'bath', 'price']].dropna()

# Convert size "3 BHK" --> 3
data['size'] = data['size'].str.extract('(\d+)').astype(float)

# Function to convert ranges & remove bad sqft data
def convert_sqft(x):
    try:
        if '-' in x:
            nums = list(map(float, x.split('-')))
            return sum(nums)/len(nums)
        return float(x)
    except:
        return np.nan

data['total_sqft'] = data['total_sqft'].apply(convert_sqft)

# Drop rows where sqft still invalid
data = data.dropna(subset=['total_sqft'])

X = data.drop(['price'], axis=1)
Y = data['price']

# Columns
categorical_features = ['location']
numerical_features = ['total_sqft', 'size', 'bath']

# Preprocessor
preprocessor = ColumnTransformer([
    ('onehot', OneHotEncoder(handle_unknown='ignore'), ['location'])
], remainder='passthrough')

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor()
}

best_score = -999
best_model_name = None
best_pipeline = None

for name, model in models.items():
    pipeline = Pipeline([('preprocessor', preprocessor),
                         ('model', model)])
    pipeline.fit(X, Y)
    preds = pipeline.predict(X)
    score = r2_score(Y, preds)
    print(f"{name} R² Score: {score:.4f}")

    if score > best_score:
        best_score = score
        best_model_name = name
        best_pipeline = pipeline

print("\nBest Model:", best_model_name)

os.makedirs("model", exist_ok=True)
pickle.dump(best_pipeline, open("model/best_model.pkl","wb"))
print("Model saved successfully with Location feature!")
