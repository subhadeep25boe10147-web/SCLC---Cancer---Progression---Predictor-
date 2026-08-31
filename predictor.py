import joblib
import pandas as pd

# Load trained model
model = joblib.load("dist/model.pkl")

print("===== Cancer Progression Predictor =====")

age = int(input("Age: "))
sex = int(input("Sex (0=Female,1=Male): "))
smoking = int(input("Smoking (0=No,1=Yes): "))
pack = float(input("Smoking Pack Years: "))
stretch = float(input("Stretch (%): "))
frequency = float(input("Frequency (Hz): "))
duration = int(input("Stretch Duration (hours): "))
fibrosis = int(input("Fibrosis Grade (0-4): "))
stiffness = float(input("Tissue Stiffness (kPa): "))
il6 = float(input("IL6: "))
vegf = float(input("VEGF: "))
ki67 = float(input("Ki67: "))
tumor = float(input("Tumor Size (cm): "))

patient = pd.DataFrame({
    "Age":[age],
    "Sex":[sex],
    "Smoking":[smoking],
    "Smoking_PackYears":[pack],
    "Stretch":[stretch],
    "Frequency":[frequency],
    "Stretch_Duration":[duration],
    "Fibrosis":[fibrosis],
    "Tissue_Stiffness":[stiffness],
    "IL6":[il6],
    "VEGF":[vegf],
    "Ki67":[ki67],
    "Tumor_Size":[tumor]
})

score = model.predict(patient)[0]

print("\nCancer Progression Score:", round(score,3))

if score < 0.30:
    print("Risk Level : LOW")
elif score < 0.60:
    print("Risk Level : MODERATE")
else:
    print("Risk Level : HIGH")


