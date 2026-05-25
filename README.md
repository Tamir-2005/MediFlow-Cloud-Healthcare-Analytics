# 🏥 MediFlow – Cloud Healthcare Analytics Project

## 📌 Project Overview
**MediFlow** is an end-to-end cloud-based healthcare analytics solution designed using modern Data Engineering and Business Intelligence practices. 

The project demonstrates how raw healthcare data can be ingested, processed, optimized, analyzed, and visualized using **AWS** cloud services and **Tableau**. It simulates a production-style healthcare analytics pipeline with secure architecture and governance compliance.

---

## 🚀 Architecture Overview 
The pipeline follows a structured, layered approach to ensure scalability and performance:
> **Raw Data (CSV)** → **Amazon S3 Data Lake** → **Parquet Optimization** → **Amazon Athena** (Serverless Query Layer) → **Analytical Dataset** → **Tableau Dashboard**
<p align="center">
  <img src="https://github.com/datadev-irfan/MediFlow-Cloud-Healthcare-Analytics/blob/main/Architecture%20diagram/architecture_diagram.png">

</p>
---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Cloud Storage** | [Amazon S3](https://aws.amazon.com) |
| **Security & IAM** | [AWS IAM](https://aws.amazon.com) |
| **Query Engine** | [Amazon Athena](https://aws.amazon.com) |
| **Optimization** | [Apache Parquet](https://parquet.apache.org) |
| **Visualization** | [Tableau Public](https://github.com/datadev-irfan/MediFlow-Cloud-Healthcare-Analytics/tree/main/dashboard) |
| **Version Control** | [GitHub](https://github.com/datadev-irfan/MediFlow-Cloud-Healthcare-Analytics) |

---

## 📊 Key Dashboard Features
*   **Total Patients & Revenue KPIs**
*   **Readmission Rate Analysis**
*   **Average Length of Stay (ALOS)**
*   **Department-wise Revenue Insights**
*   **City-wise Patient Distribution Map**
*   **Interactive Filtering** for deep-dive analysis

---

## 🔐 Data Governance & Compliance
This project adheres to strict data privacy principles:
*   **Synthetic Data:** All patient records are synthetically generated.
*   **Anonymization:** No **PII** (Personally Identifiable Information) or contact details are stored.
*   **Access Control:** Managed via **IAM policies**; no public access to S3 buckets.

---

## 🎯 Project Highlights
- [x] Designed **Layered S3 Data Lake** (Raw → Processed → Analytics).
- [x] Implemented **Parquet-based** performance and cost optimization.
- [x] Created a **Serverless Analytical Layer** using Athena.
- [x] Applied governance & security best practices for healthcare data.

---

## 👤 Author
**Tamir N**  
*Cloud & Data Analytics Enthusiast*  
*Capstone Cloud Data Engineering Internship Project*

---
