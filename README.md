📊 Data Exploration, Cleaning & Predictive Analytics with Python  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)  
![Pandas](https://img.shields.io/badge/Library-Pandas-yellow?logo=pandas)  
![NumPy](https://img.shields.io/badge/Library-NumPy-orange?logo=numpy)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  

---

## 🚀 Overview  

This project demonstrates my ability to work with **real-world datasets** by performing:  

- 🔍 **Exploration** – Identifying missing values & data issues  
- 🧹 **Cleaning** – Handling missing values dynamically (mean/mode imputation)  
- 📈 **Analysis** – Aggregating insights across regions, months & demographics  
- 🔮 **Prediction** – Forecasting September 2024 sales by region  

---

## 📂 Repository Structure  

```bash
├── EXP1_Data_Cleaning.py     # Data exploration & cleaning
├── EXP2_Data_Analysis.py     # Aggregation & monthly insights
├── EXP3_Prediction.py        # Forecasting September 2024 sales
└── README.md                 # Project documentation
🔍 EXP1: Data Exploration & Cleaning
✔️ Calculated the percentage of records with missing values
✔️ Handled missing values:

Mode for categorical columns

Mean for numerical columns
✔️ Produced a clean dataset ready for analysis

Code Snippet

python
Copy code
# Fill missing categorical with mode
for col in categorical_cols:
    if cleaned_df_filled[col].isnull().any():
        cleaned_df_filled[col].fillna(cleaned_df_filled[col].mode()[0], inplace=True)

# Fill missing numerical with mean
for col in numerical_cols:
    if cleaned_df_filled[col].isnull().any():
        cleaned_df_filled[col].fillna(cleaned_df_filled[col].mean(), inplace=True)
📈 EXP2: Data Analysis
Aggregated pre-sale orders per month grouped by region and demographic group.

Sample Output

Order Month	Region	Demographic Group	Total Pre-orders
2024-07	Europe	Casual	15
2024-07	Asia	Gamer	22
2024-07	North America	Family	18

🔮 EXP3: Predictive Analytics
Predicted September 2024 sales by region using growth rates from July → August.

Forecast Formula

𝐺
𝑟
𝑜
𝑤
𝑡
ℎ
𝑅
𝑎
𝑡
𝑒
=
(
𝐴
𝑢
𝑔
𝑢
𝑠
𝑡
𝑆
𝑎
𝑙
𝑒
𝑠
−
𝐽
𝑢
𝑙
𝑦
𝑆
𝑎
𝑙
𝑒
𝑠
)
/
(
𝐽
𝑢
𝑙
𝑦
𝑆
𝑎
𝑙
𝑒
𝑠
+
𝜀
)
𝑆
𝑒
𝑝
𝑡
𝑒
𝑚
𝑏
𝑒
𝑟
𝐹
𝑜
𝑟
𝑒
𝑐
𝑎
𝑠
𝑡
=
𝐴
𝑢
𝑔
𝑢
𝑠
𝑡
𝑆
𝑎
𝑙
𝑒
𝑠
∗
(
1
+
𝐺
𝑟
𝑜
𝑤
𝑡
ℎ
𝑅
𝑎
𝑡
𝑒
)
GrowthRate=(AugustSales−JulySales)/(JulySales+ε)SeptemberForecast=AugustSales∗(1+GrowthRate)
Sample Prediction Output

Region	September 2024 (Forecast)
Europe	45.2
Asia	38.7
North America	52.3
Oceania	27.9

🛠️ Tech Stack
Programming Language: Python 🐍

Libraries:

pandas → Data manipulation

numpy → Numerical computing

📬 Connect with Me
🌐 GitHub: MuhammadQasim111

💼 LinkedIn: Muhammad Qasim

📧 Email: mqasim111786111@gmail.com
