import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load dataset
data = pd.read_csv("data/attendance_data.csv")

# Feature (X) and Target (y)
X = data[["leaves_taken"]]   # Simple Linear Regression = ONE feature
y = data["attendance_percentage"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Simple Linear Regression Results")
print("--------------------------------")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.2f}")



print("\nMultiple Linear Regression Results")
print("--------------------------------")

# Multiple Linear Regression
X_multi = data[
    [
        "leaves_taken",
        "consecutive_leaves",
        "saturdays_off",
        "festive_holidays"
    ]
]
y = data["attendance_percentage"]

X_train, X_test, y_train, y_test = train_test_split(
    X_multi, y, test_size=0.2, random_state=42
)

multi_model = LinearRegression()
multi_model.fit(X_train, y_train)

y_pred_multi = multi_model.predict(X_test)

mae_multi = mean_absolute_error(y_test, y_pred_multi)
rmse_multi = np.sqrt(mean_squared_error(y_test, y_pred_multi))
r2_multi = r2_score(y_test, y_pred_multi)

print(f"MAE  : {mae_multi:.2f}")
print(f"RMSE : {rmse_multi:.2f}")
print(f"R²   : {r2_multi:.2f}")


from sklearn.preprocessing import PolynomialFeatures

print("\nPolynomial Regression Results")
print("-----------------------------")

# Polynomial Features (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_multi)

X_train_poly, X_test_poly, y_train_poly, y_test_poly = train_test_split(
    X_poly, y, test_size=0.2, random_state=42
)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train_poly)

y_pred_poly = poly_model.predict(X_test_poly)

mae_poly = mean_absolute_error(y_test, y_pred_poly)
rmse_poly = np.sqrt(mean_squared_error(y_test, y_pred_poly))
r2_poly = r2_score(y_test, y_pred_poly)

print(f"MAE  : {mae_poly:.2f}")
print(f"RMSE : {rmse_poly:.2f}")
print(f"R²   : {r2_poly:.2f}")

import joblib

# After training multi_model
joblib.dump(multi_model, "ml/multi_model.pkl")
print("Multiple Linear Regression model saved as multi_model.pkl")
