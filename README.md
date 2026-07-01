# AI Disease Prediction System

An interactive machine learning web application designed to predict potential diseases based on patient symptoms. This project utilizes a Naive Bayes classifier on the backend and a Streamlit interface on the frontend.

## Features
- Smart Diagnosis: Analyzes a combination of 132 different medical symptoms to predict the underlying condition.
- Interactive UI: Features a step-by-step diagnostic progress bar and smooth user feedback.
- Machine Learning Pipeline: Built using scikit-learn with proper data preprocessing and label encoding.

## Project Structure
- data/: Contains the training and testing datasets.
- notebooks/: Jupyter notebooks for data analysis, visualization, and model training.
- src/: Serialized model files, label encoders, and feature lists (.pkl).
- app.py: The main Streamlit web application script.

## Technology Stack
- Language: Python
- Machine Learning: Scikit-Learn
- Data Handling: Pandas, NumPy
- Visualization: Matplotlib, Seaborn
- Web Framework: Streamlit