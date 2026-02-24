
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# ==============================
# Currency Exchange Rates (to EGP)
# ==============================
PRICE_EXCHANGE_RATES = { "EGP": 1, 
                        "USD": 47.80, # 1 USD = 47.80 EGP 
                        "GBP": 64.48, # 1 GBP = 64.48 EGP 
                        "EUR": 56.28, # 1 EUR = 56.28 EGP 
                        "$": 47.80, #USD 
                        "£": 64.48, #GBP 
                        "€": 56.28 #EUR 
                        }


# ==============================
# Load Dataset
# ==============================

df=pd.read_csv("Amazon_Product_Dataset.csv")


# Map exchange rates to dataframe
df["Rate"] = df["Currency"].map(PRICE_EXCHANGE_RATES)

# Create new column with price converted to EGP
df["Price(EGP)"] = df["Price"] * df["Rate"]

# Remove temporary Rate column
df.drop(columns=["Rate"], inplace=True)



# ==============================
# Visualization Settings
# ==============================
sns.set_style("whitegrid")


# ==============================
# 1️⃣ Average Price Per Product
# ==============================

plt.figure(figsize=(12,6))

sns.barplot(
    data=df,
    x="Title",
    y="Price(EGP)",
    palette="Set2",
    errorbar=None
)


plt.title("Product Average Price")
plt.xlabel("Product Title")
plt.ylabel("Price (EGP)")
plt.tight_layout()
plt.show()



# ==============================
# 2️⃣ Price Trend Over Time
# ==============================
plt.figure(figsize=(12,6))

sns.lineplot(
    data=df,
    x="Date",
    y="Price(EGP)",
    hue="Title"
)

plt.title("Product Price Changes Over Time")
plt.xlabel("Date")
plt.ylabel("Price (EGP)")
plt.tight_layout()
plt.show()





