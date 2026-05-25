import pandas as pd
import numpy as np

# Load patient dataset
patient_df = pd.read_csv("C:\\Users\\mohamedirfan\\OneDrive\\Desktop\\Medi_Flow_Cloud\\data\\raw\\mediflow_dummy_dataset.csv")

# Set random seed for reproducibility
np.random.seed(42)

# Generate billing data
billing_df = pd.DataFrame()

billing_df["billing_id"] = ["BILL_" + str(i).zfill(5) for i in range(1, len(patient_df) + 1)]
billing_df["patient_id"] = patient_df["patient_id"]

# Random daily hospital rate between 2000 and 8000
daily_rate = np.random.randint(2000, 8000, size=len(patient_df))

# Treatment cost = length_of_stay × daily_rate
billing_df["treatment_cost"] = patient_df["length_of_stay"] * daily_rate

# Insurance coverage (70% to 90%)
insurance_percent = np.random.uniform(0.7, 0.9, size=len(patient_df))
billing_df["insurance_coverage"] = billing_df["treatment_cost"] * insurance_percent

# Hospital charges (10% additional admin charges)
billing_df["hospital_charges"] = billing_df["treatment_cost"] * 0.10

# Final amount patient pays
billing_df["final_amount"] = (
    billing_df["treatment_cost"]
    + billing_df["hospital_charges"]
    - billing_df["insurance_coverage"]
)

# Payment status
billing_df["payment_status"] = np.where(
    np.random.rand(len(patient_df)) > 0.1,
    "Paid",
    "Pending"
)

# Round financial columns
billing_df = billing_df.round(2)

# Save billing dataset
billing_df.to_csv("billing_data.csv", index=False)

print("Billing dataset generated successfully!")