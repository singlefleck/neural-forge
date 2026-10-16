import functions
booking_price = 12000
prices = [12000, 9500, 8700, 10500, 7600]
new_prices = [9500, 8700, 7600]

print("All prices:", prices)

def filter_prices(prices, threshold):
    for price in prices:
        if price < threshold:
            print(f"Price ₹{price} is below the threshold of ₹{threshold}")
            savings = functions.calculate_savings(booking_price, price)
            print(f"Price ₹{price} savings: ₹{savings}")


filter_prices(prices, 10000)



def filter_prices_with_list(prices, threshold):
    new_filter = []

    for price in prices:
        if price < threshold:
            new_filter.append(price)
    return new_filter


print(filter_prices_with_list(new_prices, 10000))





import json
from pathlib import Path

data_path = Path(__file__).with_name("bookings.json")

with data_path.open("r", encoding="utf-8") as file:
    data = json.load(file)

booking = data["booking"]
supplier_rates = data["supplier_rates"]

print("Hotel:", booking["hotel"])
print("Original price:", booking["price"])

for rate in supplier_rates:
    print(rate["supplier"], rate["price"])
