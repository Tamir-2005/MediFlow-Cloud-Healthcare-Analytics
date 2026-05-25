import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Number of records
n = 10000

# Departments and probabilities
departments = ["Cardiology", "Neurology", "Orthopedics", "General Medicine", "ICU", "Pediatrics"]
diagnoses = ["Diabetes", "Heart Disease", "Stroke", "Fracture", "Infection", "Hypertension"]
procedures = ["Surgery", "Medication", "Therapy", "Observation"]
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad", "Kolkata"]

data = []

for i in range(n):
    age = np.random.randint(1, 90)
    gender = random.choice(["Male", "Female"])
    department = random.choice(departments)
    diagnosis = random.choice(diagnoses)
    procedure = random.choice(procedures)
    city = random.choice(cities)
    
    admission_date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
    length_of_stay = random.randint(1, 15)
    discharge_date = admission_date + timedelta(days=length_of_stay)
    
    # Smart readmission logic
    readmit_prob = 0.1
    
    if age > 65:
        readmit_prob += 0.15
    if department in ["Cardiology", "ICU"]:
        readmit_prob += 0.15
    if length_of_stay <= 3:
        readmit_prob += 0.10
    
    readmitted = 1 if random.random() < readmit_prob else 0

    data.append([
        i+1, age, gender, department, diagnosis,
        procedure, admission_date.date(),
        discharge_date.date(), length_of_stay,
        city, readmitted
    ])

columns = [
    "patient_id", "age", "gender", "department",
    "diagnosis", "procedure", "admission_date",
    "discharge_date", "length_of_stay",
    "city", "readmitted_30_days"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("mediflow_dummy_dataset.csv", index=False)

print("Dataset generated successfully!")
