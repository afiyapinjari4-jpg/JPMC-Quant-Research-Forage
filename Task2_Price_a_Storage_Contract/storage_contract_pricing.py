import pandas as pd
from scipy.interpolate import interp1d

gas_data = pd.read_csv("Nat_Gas.csv")

gas_data["Dates"] = pd.to_datetime(gas_data["Dates"], format="%m/%d/%y")
gas_data = gas_data.sort_values("Dates")

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

def calculate_contract_value(
    injection_date,
    withdrawal_date,
    volume,
    injection_rate,
    withdrawal_rate,
    max_storage,
    storage_cost_per_month,
    injection_cost,
    withdrawal_cost
):

    if volume > max_storage:
        return "Storage capacity exceeded."

    buy_price = estimate_gas_price(injection_date)
    sell_price = estimate_gas_price(withdrawal_date)

    injection_date = pd.to_datetime(injection_date)
    withdrawal_date = pd.to_datetime(withdrawal_date)

    if withdrawal_date <= injection_date:
        return "Withdrawal date must be after injection date."

    months = (
        (withdrawal_date.year - injection_date.year) * 12
        + (withdrawal_date.month - injection_date.month)
    )

    purchase_amount = buy_price * volume
    selling_amount = sell_price * volume

    profit = selling_amount - purchase_amount

    storage_cost = months * storage_cost_per_month

    total_cost = storage_cost + injection_cost + withdrawal_cost

    final_value = profit - total_cost

    return {
        "Buy Price": round(buy_price, 2),
        "Sell Price": round(sell_price, 2),
        "Purchase Cost": round(purchase_amount, 2),
        "Selling Revenue": round(selling_amount, 2),
        "Gross Profit": round(profit, 2),
        "Storage Cost": round(storage_cost, 2),
        "Total Cost": round(total_cost, 2),
        "Contract Value": round(final_value, 2)
    }

contract = calculate_contract_value(
    injection_date="2023-05-15",
    withdrawal_date="2023-12-20",
    volume=1000000,
    injection_rate=50000,
    withdrawal_rate=50000,
    max_storage=2000000,
    storage_cost_per_month=100000,
    injection_cost=10000,
    withdrawal_cost=10000
)

print("\nNatural Gas Storage Contract\n")

if isinstance(contract, dict):
    for key, value in contract.items():
        print(f"{key}: {value}")
else:
    print(contract)