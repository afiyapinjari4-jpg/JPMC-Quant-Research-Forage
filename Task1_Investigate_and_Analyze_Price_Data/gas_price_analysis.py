import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

gas_data = pd.read_csv("Nat_Gas.csv")

gas_data["Dates"] = pd.to_datetime(gas_data["Dates"], format="%m/%d/%y")
gas_data = gas_data.sort_values("Dates")

print("First 5 rows of the dataset:")
print(gas_data.head())

date_values = gas_data["Dates"].map(pd.Timestamp.toordinal)

price_estimator = interp1d(
    date_values,
    gas_data["Prices"],
    kind="linear",
    fill_value="extrapolate"
)

def estimate_gas_price(date):
    date = pd.to_datetime(date)
    return float(price_estimator(date.toordinal()))

sample_dates = [
    "2023-05-15",
    "2025-03-20"
]

print("\nEstimated Prices")
print("-------------------------")

for date in sample_dates:
    price = estimate_gas_price(date)
    print(f"{date} : {price:.2f}")

future_dates = pd.date_range(
    start="2024-10-31",
    end="2025-09-30",
    freq="ME"
)

future_prices = [
    estimate_gas_price(date)
    for date in future_dates
]

plt.figure(figsize=(10, 5))

plt.plot(
    gas_data["Dates"],
    gas_data["Prices"],
    marker="o",
    label="Historical Prices"
)

plt.plot(
    future_dates,
    future_prices,
    marker="o",
    linestyle="--",
    label="Estimated Prices"
)

plt.title("Natural Gas Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.show()