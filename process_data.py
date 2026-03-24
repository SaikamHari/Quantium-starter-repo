import pandas as pd

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3])
df = df[df["product"] == "pink morsel"]

df["Sales"] = df["quantity"] * df["price"]

df = df[["Sales", "date", "region"]]
df.columns = ["Sales", "Date", "Region"]

df.to_csv("data/processed_data.csv", index=False)
df["Date"] = pd.to_datetime(df["Date"])

before = df[df["Date"] < "2021-01-15"]["Sales"].sum()
after = df[df["Date"] >= "2021-01-15"]["Sales"].sum()

print("Before Jan 15:", before)
print("After Jan 15:", after)
print("Program started")
print("Done ✅")