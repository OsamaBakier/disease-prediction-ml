import streamlit as st
import pickle
import pandas as pd
import numpy as np
import time

st.title("AI Disease Prediction System 🩺")
st.warning(
    "⚠️ **Disclaimer:** This application is intended for educational purposes only and should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns."
           )
st.markdown("---")

with open("src/symptom_model.pkl", "rb") as file:
    model_nb = pickle.load(file)

with open("src/label_encoder.pkl", "rb") as file:
    encoder = pickle.load(file)

with open("src/features_list.pkl", "rb") as file:
    features_list = pickle.load(file)

display_features = [symptom.replace("_", " ").title() for symptom in features_list]

st.sidebar.header("📋 Patient Inputs")
st.sidebar.write("Please select the symptoms you are experiencing:")

if st.sidebar.button("Reset Application"):
    st.rerun()

user_choices = st.sidebar.multiselect("Select your symptoms:", display_features)

if user_choices:
    input_data = np.zeros(len(features_list))

    for symptom in user_choices:

        if symptom in display_features:

            index = display_features.index(symptom)
            input_data[index] = 1
    
    input_data = input_data.reshape(1, -1)
    input_data_df = pd.DataFrame(input_data, columns=features_list)
 
    predicted_numeirc = model_nb.predict(input_data_df)
    predicted_disease = encoder.inverse_transform(predicted_numeirc)[0]

    progress_bar = st.progress(0)
    status_text = st.empty()
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete+1)
        status_text.text(f"🧠 AI Diagnosing Symptoms: {percent_complete + 1}%")
    status_text.empty()
    progress_bar.empty()
    
    with st.container(border=True):
        st.subheader("🩺 Prediction Result")
        st.divider()

        st.markdown("#### Disease")
        st.success(predicted_disease)

        st.markdown("#### Machine Learning Model")
        st.info("Naive Bayes")

else:
    st.info("👈 Select one or more symptoms from the sidebar to begin the prediction.")

st.caption("Developed by Osama Bakier")