import pandas as pd
from scipy.interpolate import interp1d

df = pd.read_csv("Nat_Gas.csv")

df["Dates"] = pd.to_datetime(df["Dates"], format="%m/%d/%y")
df = df.sort_values("Dates").reset_index(drop=True)

date_numbers = df["Dates"].map(pd.Timestamp.toordinal)

price_function = interp1d(
    date_numbers,
    df["Prices"],
    kind="linear",
    fill_value="extrapolate"
)

def get_price(date):
    date = pd.to_datetime(date)
    return float(price_function(date.toordinal()))

def price_storage_contract(
    injection_date,
    withdrawal_date,
    volume,
    injection_rate,
    withdrawal_rate,
    max_storage_volume,
    storage_cost_per_month,
    injection_cost,
    withdrawal_cost
):

    if volume > max_storage_volume:
        raise ValueError("Volume exceeds maximum storage capacity.")

    if injection_rate <= 0 or withdrawal_rate <= 0:
        raise ValueError("Injection and withdrawal rates must be positive.")

    buy_price = get_price(injection_date)
    sell_price = get_price(withdrawal_date)

    injection_date = pd.to_datetime(injection_date)
    withdrawal_date = pd.to_datetime(withdrawal_date)

    if withdrawal_date <= injection_date:
        raise ValueError("Withdrawal date must be after injection date.")

    months = (
        (withdrawal_date.year - injection_date.year) * 12
        + withdrawal_date.month
        - injection_date.month
    )

    purchase_cost = buy_price * volume
    sale_revenue = sell_price * volume

    gross_profit = sale_revenue - purchase_cost

    storage_cost = months * storage_cost_per_month

    total_cost = (
        storage_cost
        + injection_cost
        + withdrawal_cost
    )

    contract_value = gross_profit - total_cost

    return {
        "Injection Price": round(buy_price, 2),
        "Withdrawal Price": round(sell_price, 2),
        "Purchase Cost": round(purchase_cost, 2),
        "Sale Revenue": round(sale_revenue, 2),
        "Gross Profit": round(gross_profit, 2),
        "Storage Cost": round(storage_cost, 2),
        "Injection Cost": round(injection_cost, 2),
        "Withdrawal Cost": round(withdrawal_cost, 2),
        "Total Cost": round(total_cost, 2),
        "Contract Value": round(contract_value, 2)
    }

result = price_storage_contract(
    injection_date="2023-05-15",
    withdrawal_date="2023-12-20",
    volume=1000000,
    injection_rate=50000,
    withdrawal_rate=50000,
    max_storage_volume=2000000,
    storage_cost_per_month=100000,
    injection_cost=10000,
    withdrawal_cost=10000
)

print("\nCommodity Storage Contract Valuation\n")

for key, value in result.items():
    print(f"{key:<20}: {value:,.2f}")