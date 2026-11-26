import pandas as pd 

df = pd.read_csv("train.csv")
"""
print(df.head(5))
print(df.info())
print(df.describe())

print("Duplicate rows:", df.duplicated().sum())

missing =df.isnull().sum()
missing_percentage = (missing / len(df))*100
print(pd.DataFrame({
    "missing values": missing,
    "missing percentage": missing_percentage
}))
print(df["LoanAmount"].describe())

print(df["Gender"].value_counts())

print(df["Credit_History"].value_counts())

q1 = 100
q3 = 168
iqr = q3 - q1
lower = q1 - 1.5*iqr
upper =q3 + 1.5*iqr
print(f"loan amount IQR: {iqr} , lower: {lower} , upper: {upper}" )

outliers = df[df["LoanAmount"]>270]
print(outliers.shape)
print(outliers["LoanAmount"])
"""

print("Duplicate rows:", df.duplicated().sum())

missing =df.isnull().sum()
missing_percentage = (missing / len(df))*100
print(pd.DataFrame({
    "missing values": missing,
    "missing percentage": missing_percentage
}))