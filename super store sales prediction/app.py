

import streamlit as st
import pickle
import numpy as np

# Page configuration
st.set_page_config(
    page_title="BigMart Sales Prediction",
    page_icon="🛒",
    layout="centered"
)

# Load trained model and scaler
with open("bigmart_knn_model.pkl", "rb") as file:
    saved_data = pickle.load(file)

model = saved_data["model"]
scaler = saved_data["scaler"]

# Title
st.title("🛒 BigMart Outlet Sales Prediction")
st.write("Enter the feature values below to predict outlet sales.")

st.subheader("Enter Product Details")

# Input fields
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)
feature4 = st.number_input("Feature 4", value=0.0)
feature5 = st.number_input("Feature 5", value=0.0)

# Prediction
if st.button("Predict Sales"):

    # Create input array
    input_data = np.array([
        [feature1, feature2, feature3, feature4, feature5]
    ])

    try:
        # Scale input data
        input_scaled = scaler.transform(input_data)

        # Predict sales
        prediction = model.predict(input_scaled)

        # Display result
        st.success(
            f"Predicted Outlet Sales: ₹ {prediction[0]:,.2f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")
        st.warning(
            "Make sure the number of features in the application "
            "matches the number of features used during model training."
        )