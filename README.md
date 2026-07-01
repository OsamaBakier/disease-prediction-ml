# Disease Prediction ML App

A web application built with Python and Streamlit that predicts potential diseases based on patient symptoms. It uses a Naive Bayes classifier on the backend to analyze a combination of 132 different medical symptoms.

## Live Demo
Check out the live application here: 
[Disease Prediction App](https://ml-disease-detection.streamlit.app/)

## Project Structure
* data/: Training and testing datasets.
* notebooks/: Jupyter notebooks for data analysis and model training.
* src/: Serialized model files and label encoders (.pkl).
* app.py/: The main Streamlit web application.

## Tech Stack
* Python
* Streamlit
* Scikit-Learn
* Pandas & NumPy

## How to Run Locally

1. Clone the repository:
   git clone https://github.com/OsamaBakier/disease-prediction-ml.git
   cd disease-prediction-ml

2. Create and activate a virtual environment:
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate

3. Install requirements:
   pip install -r requirements.txt

4. Run the app:
   streamlit run app.py

## Author
* GitHub: @OsamaBakier