import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load trained model and preprocessor
try:
    with open("model.pkl", "rb") as model_file:
        dtr = pickle.load(model_file)

    with open("preprocessor.pkl", "rb") as preprocessor_file:
        preprocessor = pickle.load(preprocessor_file)

except Exception as e:
    st.error(f"Error loading model or preprocessor: {e}")

# Define the prediction function
def prediction(Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item):
    try:
        # Create DataFrame for input
        input_data = pd.DataFrame({
            "Year": [Year],
            "average_rain_fall_mm_per_year": [average_rain_fall_mm_per_year],
            "pesticides_tonnes": [pesticides_tonnes],
            "avg_temp": [avg_temp],
            "Area": [Area],
            "Item": [Item]
        })
        X_train=pd.read_csv(r"X_train.csv")
        y_train=pd.read_csv("y_train.csv")
        X_test=pd.read_csv("X_train.csv")
        X_train_dummy = preprocessor.fit_transform(X_train)
        X_test_dummy = preprocessor.transform(X_test)
        # Ensure input data structure matches training format
        transformed_features = preprocessor.transform(input_data)  # No extra arguments!
        dtr.fit(X_train_dummy,y_train)

        # Predict yield
        predicted_yield = dtr.predict(transformed_features)
        

        return predicted_yield[0]

    except Exception as e:
        return f"Prediction Error: {e}"


# Streamlit UI
st.title("Crop Yield Prediction")

# Input fields
Year = st.number_input("Year", min_value=1900, max_value=2100, value=1990)
average_rain_fall_mm_per_year = st.number_input("Average Rainfall (mm)", value=1485.0)
pesticides_tonnes = st.number_input("Pesticides Used (tonnes)", value=121.00)
avg_temp = st.number_input("Average Temperature (°C)", value=16.37)
Area = st.text_input("Area (Country)", "Albania")
Item = st.text_input("Crop", "Maize")

# Prediction button
if st.button("Predict Yield"):
    result = prediction(Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item)
    
    if isinstance(result, str):  
        st.error(result)  # Show error message if prediction fails
    else:
        st.success(f"Predicted Crop Yield: {result:.2f} tons/hectare")
