import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error

import joblib

# Load Dataset
data = pd.read_csv("dataset.csv")

# Input Features
X = data.drop(["Patient_ID","CPS"], axis=1)

# Target
y = data["CPS"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, predictions)

print("Mean Squared Error:", mse)

# Save Model
joblib.dump(model, "dist/model.pkl")

print("Model Saved Successfully")