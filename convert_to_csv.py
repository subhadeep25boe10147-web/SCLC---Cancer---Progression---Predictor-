import pandas as pd

# Read Excel file
data = pd.read_excel("SCLC_Cyclic_Mechanical_Stretch_Synthetic_Dataset_5000.xlsx")

# Save as CSV
data.to_csv("dataset.csv", index=False)

print("CSV file created successfully!")