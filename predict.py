import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Load the saved model and transformers
with open('model/svr_model.pkl', 'rb') as f:
    regressor = pickle.load(f)

with open('model/scaler_x.pkl', 'rb') as f:
    scaler_x = pickle.load(f)

with open('model/scaler_y.pkl', 'rb') as f:
    scaler_y = pickle.load(f)

with open('model/column_transformer.pkl', 'rb') as f:
    column_transformer = pickle.load(f)

# Function to predict price based on input
def predict_price(view, size, year):
    # Prepare input data
    input_df = pd.DataFrame([[view, size, year]], columns=["view", "size", "year"])
    
    # Transform the input data
    input_transformed = column_transformer.transform(input_df)
    
    # Standardize the input data
    input_transformed[:, 1:] = scaler_x.transform(input_transformed[:, 1:])
    
    # Predict the scaled price
    predicted_price_scaled = regressor.predict(input_transformed).reshape(-1, 1)
    
    # Inverse transform to get the actual price
    predicted_price = scaler_y.inverse_transform(predicted_price_scaled)[0][0]
    predicted_price = f"${predicted_price:,.2f}"
    
    return predicted_price

# Example prediction
if __name__ == "__main__":
    # Test the function with an example (will only execute if script runs directly no worries)
    predicted_price = predict_price("Sea view", 1033, 2013)
    print(f"Predicted price: ${predicted_price:,.2f}")
