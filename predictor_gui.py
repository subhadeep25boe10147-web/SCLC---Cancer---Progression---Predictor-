import tkinter as tk
from tkinter import messagebox

import joblib
import pandas as pd
import os
# ==========================
# Load Model
# ==========================
try:
    model = joblib.load("dist/model.pkl")
except:
    messagebox.showerror("Error", "model.pkl not found.\nRun train_model.py first.")
    exit()

# ==========================
# Prediction Function
# ==========================
def predict():
    try:
        patient = pd.DataFrame({
            "Age": [int(age_var.get())],
            "Sex": [int(sex_var.get())],
            "Smoking": [int(smoking_var.get())],
            "Smoking_PackYears": [float(pack_var.get())],
            "Stretch": [float(stretch_var.get())],
            "Frequency": [float(freq_var.get())],
            "Stretch_Duration": [int(duration_var.get())],
            "Fibrosis": [int(fibrosis_var.get())],
            "Tissue_Stiffness": [float(stiffness_var.get())],
            "IL6": [float(il6_var.get())],
            "VEGF": [float(vegf_var.get())],
            "Ki67": [float(ki67_var.get())],
            "Tumor_Size": [float(tumor_var.get())]
        })

        score = float(model.predict(patient)[0])

        score_label.config(text=f"{score:.3f}")

        if score < 0.30:
            risk = "LOW RISK"
            color = "green"
        elif score < 0.60:
            risk = "MODERATE RISK"
            color = "orange"
        else:
            risk = "HIGH RISK"
            color = "red"

        risk_label.config(text=risk, fg=color)

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# ==========================
# Clear Function
# ==========================
def clear():
    variables = [
        age_var, sex_var, smoking_var, pack_var,
        stretch_var, freq_var, duration_var,
        fibrosis_var, stiffness_var, il6_var,
        vegf_var, ki67_var, tumor_var
    ]

    for var in variables:
        var.set("")

    score_label.config(text="0.000")
    risk_label.config(text="------", fg="black")

# ==========================
# Main Window
# ==========================
root = tk.Tk()
root.title("AI Cancer Progression Predictor")
root.geometry("1300x1200")
root.configure(bg="#F5F7FA")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Cancer Progression Predictor",
    font=("Segoe UI", 20, "bold"),
    bg="#F5F7FA",
    fg="#003366"
)
title.pack(pady=10)

subtitle = tk.Label(
    root,
    text="Artificial Intelligence using Random Forest",
    font=("Segoe UI", 11),
    bg="#F5F7FA"
)
subtitle.pack()

frame = tk.Frame(root, bg="#F5F7FA")
frame.pack(pady=20)

# ==========================
# Variables
# ==========================
age_var = tk.StringVar()
sex_var = tk.StringVar()
smoking_var = tk.StringVar()
pack_var = tk.StringVar()
stretch_var = tk.StringVar()
freq_var = tk.StringVar()
duration_var = tk.StringVar()
fibrosis_var = tk.StringVar()
stiffness_var = tk.StringVar()
il6_var = tk.StringVar()
vegf_var = tk.StringVar()
ki67_var = tk.StringVar()
tumor_var = tk.StringVar()

fields = [
    ("Age", age_var),
    ("Sex (0=Female,1=Male)", sex_var),
    ("Smoking (0=No,1=Yes)", smoking_var),
    ("Smoking Pack Years", pack_var),
    ("Stretch (%)", stretch_var),
    ("Frequency (Hz)", freq_var),
    ("Stretch Duration (Hours)", duration_var),
    ("Fibrosis Grade", fibrosis_var),
    ("Tissue Stiffness (kPa)", stiffness_var),
    ("IL6", il6_var),
    ("VEGF", vegf_var),
    ("Ki67", ki67_var),
    ("Tumor Size (cm)", tumor_var)
]

for i, (text, var) in enumerate(fields):
    tk.Label(
        frame,
        text=text,
        bg="#F5F7FA",
        font=("Segoe UI", 10)
    ).grid(row=i, column=0, sticky="w", pady=5)

    tk.Entry(
        frame,
        textvariable=var,
        width=20,
        font=("Segoe UI", 10)
    ).grid(row=i, column=1, padx=10)

# ==========================
# Buttons
# ==========================
button_frame = tk.Frame(root, bg="#F5F7FA")
button_frame.pack()

tk.Button(
    button_frame,
    text="Predict",
    width=15,
    bg="#007ACC",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=predict
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Clear",
    width=15,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=clear
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="Exit",
    width=15,
    bg="#D32F2F",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=root.destroy
).grid(row=0, column=2, padx=10)

# ==========================
# Result
# ==========================
result_frame = tk.LabelFrame(
    root,
    text="Prediction Result",
    font=("Segoe UI", 12, "bold"),
    bg="#F5F7FA"
)
result_frame.pack(padx=20, pady=25, fill="x")

tk.Label(
    result_frame,
    text="Cancer Progression Score",
    font=("Segoe UI", 11),
    bg="#F5F7FA"
).pack(pady=5)

score_label = tk.Label(
    result_frame,
    text="0.000",
    font=("Segoe UI", 24, "bold"),
    fg="#003366",
    bg="#F5F7FA"
)
score_label.pack()

tk.Label(
    result_frame,
    text="Risk Level",
    font=("Segoe UI", 11),
    bg="#F5F7FA"
).pack()

risk_label = tk.Label(
    result_frame,
    text="------",
    font=("Segoe UI", 18, "bold"),
    bg="#F5F7FA"
)
risk_label.pack(pady=10)

footer = tk.Label(
    root,
    text="Developed using Python | Tkinter | Scikit-Learn | Random Forest",
    font=("Segoe UI", 9),
    bg="#F5F7FA",
    fg="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()

