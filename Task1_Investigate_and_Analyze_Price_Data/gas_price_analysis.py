import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d



df = pd.read_csv("Nat_Gas.csv")


df["Dates"] = pd.to_datetime(df["Dates"], format="%m/%d/%y")


df = df.sort_values("Dates")


print("First 5 rows of the dataset:")
print(df.head())


plt.figure(figsize=(12, 5))
plt.plot(df["Dates"], df["Prices"], marker="o", label="Historical Prices")
plt.title("Natural Gas Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.show()


date_numbers = df["Dates"].map(pd.Timestamp.toordinal)

price_function = interp1d(
    date_numbers,
    df["Prices"],
    kind="linear",
    fill_value="extrapolate"
)


monthly_avg = df.groupby(df["Dates"].dt.month)["Prices"].mean()

trend = (df["Prices"].iloc[-1] - df["Prices"].iloc[-13]) / 12


last_date = df["Dates"].max()

future_dates = pd.date_range(
    start=last_date + pd.offsets.MonthEnd(1),
    periods=12,
    freq="ME"
)

future_prices = []

for i, d in enumerate(future_dates):
    seasonal_price = monthly_avg[d.month]
    estimated_price = seasonal_price + trend * (i + 1)
    future_prices.append(estimated_price)

future_df = pd.DataFrame({
    "Dates": future_dates,
    "Prices": future_prices
})



combined = pd.concat([df, future_df], ignore_index=True)

combined_dates = combined["Dates"].map(pd.Timestamp.toordinal)

combined_function = interp1d(
    combined_dates,
    combined["Prices"],
    kind="linear",
    fill_value="extrapolate"
)



def estimate_price(date):
    """
    Returns estimated natural gas price for any date.
    Example:
        estimate_price("2025-03-20")
    """
    d = pd.to_datetime(date)
    return round(float(combined_function(d.toordinal())), 2)



print("\nEstimated Prices")
print("----------------------------")
print("2023-05-15 :", estimate_price("2023-05-15"))
print("2025-03-20 :", estimate_price("2025-03-20"))

plt.figure(figsize=(12, 5))

plt.plot(
    df["Dates"],
    df["Prices"],
    marker="o",
    label="Historical"
)

plt.plot(
    future_df["Dates"],
    future_df["Prices"],
    marker="o",
    label="Forecast"
)

plt.title("Historical and Forecast Gas Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.show()