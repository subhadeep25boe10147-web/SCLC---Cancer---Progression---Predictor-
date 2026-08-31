# SCLC Cancer Progression Predictor

An AI-based machine learning project for predicting the Cancer Progression Score (CSP) in Small Cell Lung Cancer (SCLC). 

This repository contains the training dataset, the machine learning model, and a user-friendly graphical interface built in Python to make predictions easily accessible.

## 🚀 Features
* **Machine Learning Model:** Pre-trained model (`model.pkl`) to evaluate and predict progression scores based on dataset parameters.
* **Graphical User Interface (GUI):** A clean, desktop-based interface for inputting data and receiving instant predictions.
* **Standalone Executable:** Available as a compiled `.exe` file so users can run the predictor without installing Python.

## 📂 Project Structure
* `predictor_gui.py` - The main script containing the user interface.
* `train_model.py` - Script used to train the machine learning model.
* `predictor.py` - Core logic for generating predictions.
* `dataset.csv` - The dataset used to train the AI model.
* `requirements.txt` - List of required Python libraries and dependencies.
* `dist/predictor_gui.exe` - The compiled, ready-to-run Windows executable application.

## 💻 How to Run (For Developers)
If you want to view or modify the source code, you can run the project locally using Python.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/subhadeep25boe10147-web/SCLC--Cancer--Progression--Predictor.git](https://github.com/subhadeep25boe10147-web/SCLC--Cancer--Progression--Predictor.git)
   cd SCLC--Cancer--Progression--Predictor
  ** bash
  pip install -r requirements.txt
  ** bash 
  python predictor_gui.py
