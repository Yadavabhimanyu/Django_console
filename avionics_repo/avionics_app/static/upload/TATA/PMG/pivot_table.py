import pandas as pd


# creating dataframe
df = pd.read_excel(r"G:\excel_basic\lot3_age_updated.xlsx")
print(df.head())
print(df.columns)

pivot=df.pivot_table(index=['Project def.'])
print(pivot)
