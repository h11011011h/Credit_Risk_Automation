import pandas as pd

# 1. Create a small sample of credit data
data = {
    'Customer_ID': [101, 102, 103, 104],
    'Credit_Score': [720, 640, 580, 800],
    'Debt_to_Income': [0.30, 0.45, 0.55, 0.15]
}

df = pd.DataFrame(data)

# 2. Create a 'Risk_Level' column based on logic
# If Score > 700 and DTI < 0.40, then 'Low Risk'
def assess_risk(row):
    if row['Credit_Score'] > 700 and row['Debt_to_Income'] < 0.40:
        return 'Low Risk'
    else:
        return 'High Risk'

df['Risk_Status'] = df.apply(assess_risk, axis=1)

# 3. Print the results
print("--- Credit Risk Analysis Results ---")
print(df)